
from app import api
from flask import request
from flask_restx import Resource
from app.schemas.roles_schema import RolesRequestSchema
from app.controllers.roles_controller import RolesController

# ?crear modulo de usuarios
roles_ns = api.namespace(
    name='Roles',
    description='Rutas del modulo Roles',
    # *llamda de todas las rutas con el contexto /global
    # localhost:5000/global
    # contexto /usuers
    path='/roles'
)

request_schema = RolesRequestSchema(roles_ns)

# ? Rutas Usuarios para OBTENER


@roles_ns.route('/')
class Roles(Resource):
    def get(self):
        '''Listar todos los roles'''
        controller = RolesController()
        return controller.all()

    @api.expect(request_schema.create(), validate=True)
    def post(self):
        # describimos en swagger
        '''Creacion de Roles'''
        # * hacemos un request del body
        controler = RolesController()
        return controler.create(request.json)

# ? Rutas Usuarios para CREAR MODIFICAR


@roles_ns.route('/<int:id>')
class rolesGetById(Resource):
    def get(self, id):
        '''Obtener un rol por el ID'''
        controller = RolesController()
        return controller.getById(id)

    @api.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar un rol por el ID'''
        controller = RolesController()
        return controller.update(id, request.json)

    def delete(self, id):
        '''Desabilitare rol por ID'''
        controller = RolesController()
        return controller.delete(id)


api.add_namespace(roles_ns)
