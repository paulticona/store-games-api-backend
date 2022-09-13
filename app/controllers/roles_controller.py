from ast import Str
from pyexpat import model
from tkinter import E
from app import db
from app.models.roles_model import RoleModel

class RolesControler:
    def __init__(self):
        self.model = RoleModel

    def create(self, data):
        try:

            new_record = self.model.create(**data) #key=valuye key=value1 ...key=valuen
            #* agregamos la data a la DB mediente la conneccion 
            db.session.add(new_record)
            db.session.commit()          

            return{
                'message': 'el rol se creo con exito',
                'data': {}
            }, 201
        except Exception as e:
            db.session.rollback()
            return{
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500