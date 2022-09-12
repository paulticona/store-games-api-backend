
from enum import unique
from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey


class UserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    last_name = Column(String(160))

    username = Column(String(80), unique=True)
    password = Column(String(120), nullable=False)

    email = Column(String(120), unique=True)

    rol_id = Column(Integer, ForeignKey('roles.id'), default=1)
