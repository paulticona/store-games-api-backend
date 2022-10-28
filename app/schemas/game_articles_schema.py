from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.game_articles_model import GameArticleModel


class GameArticlesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Game Article Create', {
            'name': fields.String(required=True, min_length=2, max_length=120), 
        })

    def update(self):
        return self.namespace.model('Game Article Update', {
            'name': fields.String(required=False, min_length=2, max_length=120),
        })


class GameArticlesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GameArticleModel
        ordered = True