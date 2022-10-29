from app.models.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, String, Text, Float, ForeignKey, Date
from sqlalchemy.orm import relationship

class WalletAccountModel(BaseModel):
    __tablename__ = 'wallet_account'
    id= Column(Integer, primary_key=True, autoincrement=True)
    cardholder = Column(String(255)) # Titular de la tarjeta
    type = Column(String(120))
    card_number = Column(Integer)
    date_expiry = Column(Date)
    cvv = Column(Integer)
    status = Column(Boolean, default=True)

    wallet = relationship('WalletModel', uselist=False, back_populates='transaction_account')