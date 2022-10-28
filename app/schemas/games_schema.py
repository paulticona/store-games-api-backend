from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.games_model import GameModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage


class GameRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        parser = RequestParser()
        parser.add_argument('title', type=str, required=True, location='form')
        parser.add_argument('description', type=str, required=True, location='form')
        parser.add_argument('gender', type=str, required=True, location='form')
        parser.add_argument('image', type=FileStorage, required=True, location='files')
        parser.add_argument('price', type=float, required=True, location='form')
        parser.add_argument('gameurl', type=str, required=True, location='form')
        parser.add_argument('platform', type=str, required=True, location='form')
        parser.add_argument('publisher', type=str, required=True, location='form')
        parser.add_argument('developer', type=str, required=True, location='form')
        parser.add_argument('release_date', type=str, required=True, location='form')
        parser.add_argument('category_id', type=int, required=True, location='form')
        return parser

    def update(self):
        parser = RequestParser()
        parser.add_argument('title', type=str, required=False, location='form')
        parser.add_argument('description', type=str, required=False, location='form')
        parser.add_argument('gender', type=str, required=False, location='form')
        parser.add_argument('image', type=FileStorage, required=False, location='files')
        parser.add_argument('price', type=float, required=False, location='form')
        parser.add_argument('gameurl', type=str, required=False, location='form')
        parser.add_argument('platform', type=str, required=False, location='form')
        parser.add_argument('publisher', type=str, required=False, location='form')
        parser.add_argument('developer', type=str, required=False, location='form')
        parser.add_argument('release_date', type=str, required=False, location='form')
        parser.add_argument('category_id', type=int, required=False, location='form')
        return parser


class GameResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GameModel
        ordered = True