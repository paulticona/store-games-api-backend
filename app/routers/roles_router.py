
from app import api
from flask_restx import Resource
from app.schemas.roles_schema import RolesRequestSchema

# ?crear modulo de usuarios
roles_ns = api.namespace(
    name='Roles',
    description='Rutas de Roles',
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
        return {
            'message':  'hola Usuario',
        }
    @api.expect(request_schema.create(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ), validate=True)
    def post(self):
        # describimos en swagger
        '''Creacion de Roles'''

        return {
            'message': 'hola Usuario',
        }

# ? Rutas Usuarios para CREAR MODIFICAR


@roles_ns.route('/<int:id>')
class rolesGetById(Resource):
    def get(self, id):
        return {
            'message': f'ID: {id}',
        }

    def put(self, id):
        return {
            'message': f'UPDATE ID: {id}',
        }

    def delete(self, id):
        return {
            'message': f'DELETE ID: {id}',
        }


api.add_namespace(roles_ns)
