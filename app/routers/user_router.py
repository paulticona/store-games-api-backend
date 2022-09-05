from app import api
from flask_restx import Resource

# ?crear modulo de usuarios
usuarios_ns = api.namespace(
    name='Usuarios',
    description='Rutas de usuarios',
    # *llamda de todas las rutas con el contexto /global
    # localhost:5000/global
    # contexto /usuers
    path='/users'
)
# ? Rutas Usuarios para OBTENER


@usuarios_ns.route('/')
class Usuario(Resource):
    def get(self):
        return {
            'message':  'hola Usuario',
        }

    def post(self):
        return {
            'message': 'hola Usuario',
        }
# ? Rutas Usuarios para CREAR MODIFICAR


@usuarios_ns.route('/<int:id>')
class UsuariosGetById(Resource):
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


api.add_namespace(usuarios_ns)
