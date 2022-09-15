from app import api
from flask_restx import Resource
from app.schemas.auth_schema import AuthRequestSchema
from app.controllers.auth_controller import AuthController
from flask import request

auth_ns = api.namespace(
    name = 'Autenticacion',
    description = 'Rutas del modulo de autenticación',
    path='/auth'
)

request_schema = AuthRequestSchema(auth_ns)

@auth_ns.route('/signin')
class Signin(Resource):

    @api.expect(request_schema.signIn(), validate=True)
    def post(self):
       '''Crear token de autenticación''' 
       controller = AuthController()
       return controller.signIn(request.json)

api.add_namespace(auth_ns)