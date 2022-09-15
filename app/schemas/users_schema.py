from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.users_model import UserModel
from flask_restx.reqparse import RequestParser


class UsersRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('User Create', {
            'name': fields.String(required=True, min_length=2, max_length=120),
            'last_name': fields.String(required=True, min_length=2, max_length=160),
            'username': fields.String(required=True, min_length=2, max_length=80),
            'password': fields.String(required=True, min_length=5, max_length=120),
            'email': fields.String(required=True, min_length=3, max_length=120),
            'rol_id': fields.Integer(readonly=True, default=2)
        })

    def update(self):
        return self.namespace.model('User Update', {
            'name': fields.String(required=False, max_length=120),
            'last_name': fields.String(required=False, max_length=160),
            'username': fields.String(required=False, max_length=80),
            'password': fields.String(required=False, max_length=120),
            'email': fields.String(required=False,  max_length=120)
        })

# * serializar los objetos del modelo


class UsersResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        ordered = True
    roles = Nested('RolesResponseSchema', exclude=['users'], many=False)
