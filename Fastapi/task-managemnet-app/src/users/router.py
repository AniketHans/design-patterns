from fastapi import APIRouter, Depends, status, Request
from src.users.dtos import UserSchema
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.users import controller
from src.users.dtos import UserResponseSchema, LoginSchema

user_router = APIRouter(prefix="/users")

@user_router.post("/register", status_code= status.HTTP_201_CREATED, response_model= UserResponseSchema)
def register_user(body: UserSchema, db: Session = Depends(get_db)):
    return controller.register(body, db)

@user_router.post("/login", status_code=status.HTTP_200_OK)
def login_user(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login(body, db)

@user_router.get("/is_auth", status_code=status.HTTP_200_OK, response_model=UserResponseSchema)
def login_user(request: Request, db: Session = Depends(get_db)):
    return controller.is_auth(request, db)