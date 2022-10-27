from app.models.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import relationship

class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(120))
    status = Column(Boolean, default=True)

    games = relationship('GameModel', uselist=True, back_populates='category')