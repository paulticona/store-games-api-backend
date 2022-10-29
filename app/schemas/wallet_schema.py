from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.wallet_model import WalletModel
from marshmallow.fields import Nested


class WalletRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Wallet Create', {
            'balance': fields.Float(required=True, min_length=2, max_length=120),
            'user_id': fields.Integer(required=True, min_length=2, max_length=120, min=1),
            'wallet_account_id': fields.Integer(required=True, min_length=2, max_length=120, min=1),
        })

    def update(self):
        return self.namespace.model('Wallet Update', {
            'balance': fields.Float(required=False, min_length=2, max_length=120),
            'user_id': fields.Integer(required=False, min_length=2, max_length=120, min=1),
            'wallet_account_id': fields.Integer(required=False, min_length=2, max_length=120, min=1),
        })


class WalletResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WalletModel
        ordered = True

    transaction_account = Nested('WalletAccountResponseSchema', many=False)
