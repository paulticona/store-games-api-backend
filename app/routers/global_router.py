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
    

api.add_namespace(global_ns)
