from src.users.models import UserModel
from sqlalchemy.orm import Session
from fastapi import Request, HTTPException, Depends
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.db import get_db
from datetime import datetime
from src.utils.settings import settings

def is_auth(request:Request, db: Session = Depends(get_db)):
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