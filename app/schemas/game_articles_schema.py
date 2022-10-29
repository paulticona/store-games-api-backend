from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.game_articles_model import GameArticleModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage


class GameArticlesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        parser = RequestParser()
        parser.add_argument('quantity', type=int, required=True, location='form')
        parser.add_argument('title', type=str, required=True, location='form')
        parser.add_argument('image', type=FileStorage, required=True, location='files')
        parser.add_argument('description', type=str, required=True, location='form')
        parser.add_argument('price', type=float, required=True, location='form')
        parser.add_argument('games_id', type=int, required=True, location='form')
        return parser

    def update(self):
        parser = RequestParser()
        parser.add_argument('quantity', type=int, required=False, location='form')
        parser.add_argument('title', type=str, required=False, location='form')
        parser.add_argument('image', type=FileStorage, required=False, location='files')
        parser.add_argument('description', type=str, required=False, location='form')
        parser.add_argument('price', type=float, required=False, location='form')
        parser.add_argument('games_id', type=int, required=False, location='form')
        return parser


class GameArticlesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GameArticleModel
        ordered = True