from app.models.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

class ShoppingCartModel(BaseModel):
    __tablename__ = 'shopping_cart'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    games_id = Column(Integer, ForeignKey('games.id'))
    article_id = Column(Integer, ForeignKey('game_articles.id'))

    game = relationship('GameModel', uselist=False, back_populates='shopping_cart')
    article = relationship('GameArticleModel', uselist=False, back_populates='shopping_cart')
