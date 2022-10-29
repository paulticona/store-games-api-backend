from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.wallet_account_model import WalletAccountModel


class WalletAccountRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Wallet Account Create', {
            'cardholder': fields.String(required=True, min_length=2, max_length=255),
            'type': fields.String(required=True, min_length=2, max_length=120),
            'card_number': fields.Integer(required=True, min_length=2, max_length=20),
            'date_expiry': fields.Date(required=True, format='%d-%m-%Y'),
            'cvv': fields.Integer(required=True, min_length=3, max_length=4),
        })

    def update(self):
        return self.namespace.model('Wallet Account Update', {
            'cardholder': fields.String(required=False, min_length=2, max_length=255),
            'type': fields.String(required=False, min_length=2, max_length=120),
            'card_number': fields.Integer(required=False, min_length=2, max_length=20),
            'date_expiry': fields.Date(required=False, format='%d-%m-%Y'),
            'cvv': fields.Integer(required=False, min_length=3, max_length=4),
        })


class WalletAccountResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WalletAccountModel
        ordered = True
