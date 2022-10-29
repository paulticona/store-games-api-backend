from app.models.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

class GameArticleModel(BaseModel):
    __tablename__ = 'game_articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer) # esto seria la cantidad de un mismo articulo puesto a la venta por varios usuarios
    title = Column(String(255))
    image = Column(String(255))
    description = Column(Text)
    price = Column(Float(precision=2))
    games_id = Column(Integer, ForeignKey('games.id'))
    status = Column(Boolean, default=True)

    game_articles = relationship('GameModel', uselist=False, back_populates='articles')
    inventory = relationship('InventoryModel', uselist=False, back_populates='game_articles')