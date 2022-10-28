from app.models.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, String, Text, Float, ForeignKey, Date
from sqlalchemy.orm import relationship

class GameModel(BaseModel):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    description = Column(Text)
    gender = Column(String)
    image = Column(String(255))
    price = Column(Float(precision=2))
    gameurl = Column(String)
    platform = Column(String)
    publisher = Column(String)
    developer = Column(String)
    release_date = Column(Date)
    category_id = Column(Integer, ForeignKey('categories.id'))
    status = Column(Boolean, default=True)

    category = relationship('CategoryModel', uselist=False, back_populates='games')
    articles = relationship('GameArticleModel', uselist=True, back_populates='game_articles')
    inventory_game = relationship('InventoryModel', uselist=True, back_populates='games_inventory')
    shopping_cart = relationship('ShoppingCartModel', uselist=True, back_populates='game')