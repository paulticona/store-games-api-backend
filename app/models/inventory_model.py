from app.models.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

class InventoryModel(BaseModel):

    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer)
    article_id = Column(Integer, ForeignKey('game_articles.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    status = Column(Boolean, default=True)

    game_articles = relationship('GameArticleModel', uselist=True, back_populates='inventory')
    games = relationship('GameModel', uselist=False, back_populates='inventory')
    users = relationship('UserModel', uselist=False, back_populates='inventory')