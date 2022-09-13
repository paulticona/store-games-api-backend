from ast import Str
from pyexpat import model
from tkinter import E
from urllib import response
from app import db
from app.models.roles_model import RoleModel
from app.schemas.roles_schema import RolesResponseSchema


class RolesControler:
    def __init__(self):
        self.model = RoleModel

    def create(self, data):
        try:

            # key=valuye key=value1 ...key=valuen
            new_record = self.model.create(**data)
            # * agregamos la data a la DB mediente la conneccion
            db.session.add(new_record)
            db.session.commit()

            response = RolesResponseSchema(many=False)
            return {
                'message': 'el rol se creo con exito',
                'data': response.dump(new_record)
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500