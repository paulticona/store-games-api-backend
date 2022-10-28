from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.schemas.games_schema import GameRequestSchema
from app.controllers.games_controller import GameController

namespace = api.namespace(
    name='Games',
    description='Endpoints para las Games',
    path='/games'
)

request_schema = GameRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Games(Resource):
    @jwt_required()
    def get(self):
        '''Listar todas los Games'''
        controller = GameController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear un Game'''
        form = request_schema.create().parse_args()
        controller = GameController()
        return controller.create(form)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class GamesById(Resource):
    @jwt_required()
    def get(self, id):
        '''Obtener un Game por el ID'''
        controller = GameController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar un Game por el ID'''
        form = request_schema.update().parse_args()
        controller = GameController()
        return controller.update(id, form)

    @jwt_required()
    def delete(self, id):
        '''Desabilitar un Game por el ID'''
        controller = GameController()
        return controller.delete(id)


api.add_namespace(namespace)
