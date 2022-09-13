from unittest.util import _MAX_LENGTH
from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.roles_model import RoleModel


class RolesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Role Create', {
            'name': fields.String(required=True, max_length=120)
        })

#* serializar los objetos del modelo
class RolesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RoleModel
