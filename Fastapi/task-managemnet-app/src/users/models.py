from sqlalchemy import Column, Integer, String, DateTime, Boolean
from src.utils.db import Base

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, nullable=False, unique=True)
    hash_password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

