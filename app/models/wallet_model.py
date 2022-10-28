from app.models.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship


class WalletModel(BaseModel):
    __tablename__ = 'wallet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Integer)  # Saldo
    user_id = Column(Integer, ForeignKey('users.id'))
    wallet_account_id = Column(Integer, ForeignKey('wallet_account.id'))

    transaction_account = relationship(
        'WalletAccountModel', uselist=False, back_populates='wallet')
    wallet_user = relationship('UserModel', uselist=False, back_populates='user_wallet')
