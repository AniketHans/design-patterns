from src.users.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException, Request
from src.users.models import UserModel
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.settings import settings
from datetime import datetime, timedelta

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(password, hash_password):
    return password_hash.verify(password, hash_password)

def register(body:UserSchema, db: Session ):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(status_code=400, detail="username already exists")
    
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(status_code=400, detail="user email already exists")
    
    hash_password = get_password_hash(body.password)
    
    newUser = UserModel(
        name = body.name,
        username = body.username,
        hash_password = hash_password,
        email = body.email
    )
    
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    
    return newUser


def login(body: LoginSchema, db: Session):
    user = db.query(UserModel).filter( UserModel.username == body.username).first()
    if not user:
        raise HTTPException(400, "user does not exist")
    if not verify_password(body.password, user.hash_password):
        raise HTTPException(401, "username or password mismatch")
    
    token_expiry_time = int((datetime.now() + timedelta(minutes=settings.JWT_TOKEN_EXPIPRY_DURATION)).timestamp())
    # token_expiry_time = int((datetime.now() + timedelta(seconds=40)).timestamp())
    jwt_token = jwt.encode({"_id": user.id, "expiry_time": token_expiry_time }, settings.JWT_SECRET, settings.ALGORITHM)
    
    return {"token": jwt_token}
    

def is_auth(request:Request, db: Session):
    try:
        token = request.headers.get("Authorization")
        if not token:
            raise InvalidTokenError()
        
        token = jwt.decode(token, settings.JWT_SECRET, settings.ALGORITHM)
        if token["expiry_time"] < datetime.now().timestamp():
            raise InvalidTokenError()
        user = db.query(UserModel).filter(UserModel.id == token["_id"]).first()
        if not user:
            raise InvalidTokenError()
        return user
    except InvalidTokenError:
        raise HTTPException(401, "Unauthorized")
    