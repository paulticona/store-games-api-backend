from app import api
from flask_restx import Resource

# crear modulo name-espace
global_ns = api.namespace(
    name='Global',
    description='Rutas globales',
    # *llamda de todas las rutas con el contexto /global
    # localhost:5000/global
    path='/globals'
)

# crear decorador
# localhost:5000/global -> GET
# localhost:5000/global -> POST
# localhost:5000/global -> PUT
# localhost:5000/global -> DELETE


## ? Rutas globales para OBTENER
@global_ns.route('/')
class Global(Resource):
    def get(self):
        return {
            'message':  'hola GET',
        }
    def post(self):
        return {
            'message': 'hola POST',
        }
## ? Rutas globales para CREAR MODIFICAR
@global_ns.route('/<int:id>')
class GlobalGetById(Resource):
    def get(self, id):
        return{
            'message': f'ID: {id}',
        }
    def put(self, id):
        return{
            'message': f'UPDATE ID: {id}',
        }
    def delete(self, id):
        return{
            'message': f'DELETE ID: {id}',
        }  
api.add_namespace(global_ns)
