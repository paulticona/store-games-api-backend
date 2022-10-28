from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.games_model import GameModel


class GameRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Categories Create', {
            'name': fields.String(required=True, min_length=2, max_length=120), 
        })

    def update(self):
        return self.namespace.model('Categories Update', {
            'name': fields.String(required=False, min_length=2, max_length=120),
        })


class GameResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GameModel
        ordered = True