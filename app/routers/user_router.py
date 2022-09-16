from app import api
from flask import request
from flask_restx import Resource
from app.schemas.users_schema import UsersRequestSchema
from app.controllers.user_controller import UsersController
from flask_jwt_extended import jwt_required

# ?crear modulo de usuarios
usuarios_ns = api.namespace(
    name='Usuarios',
    description='Rutas de usuarios',
    # *llamda de todas las rutas con el contexto /global
    # localhost:5000/global
    # contexto /usuers
    path='/users'

)
request_schema = UsersRequestSchema(usuarios_ns)
# ? Rutas Usuarios para OBTENER

# ! video 02:15:00


@usuarios_ns.route('/')
@usuarios_ns.doc(security='Bearer')
class Usuario(Resource):
    @jwt_required()
    @usuarios_ns.expect(request_schema.all())
    def get(self):
        '''Listar Usuarios'''
        query_params  = request_schema.all().parse_args()
        controller = UsersController()
        return controller.all(query_params['page'], query_params['per_page'])

    @jwt_required()
    @api.expect(request_schema.create(), validate=True)
    def post(self):
        # describimos en swagger
        '''Creacion de Usuarios'''
        # * hacemos un request del body
        controler = UsersController()
        return controler.create(request.json)
# ? Rutas Usuarios para CREAR MODIFICAR


@usuarios_ns.route('/<int:id>')
@usuarios_ns.doc(security='Bearer')
class usuariosGetById(Resource):
    @jwt_required()
    def get(self, id):
        '''Obtener un user por el ID'''
        controller = UsersController()
        return controller.getById(id)
        
    @jwt_required()
    @api.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar un User por el ID'''

        controller = UsersController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        '''Desabilitare User por ID'''
        controller = UsersController()
        return controller.delete(id)


api.add_namespace(usuarios_ns)
