from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.schemas.game_articles_schema import GameArticlesRequestSchema
from app.controllers.game_articles_controller import GameArticlesController

namespace = api.namespace(
    name='Artículos de los Juegos',
    description='Endpoints para las Games Articles',
    path='/game_articles'
)

request_schema = GameArticlesRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class GameArticles(Resource):
    @jwt_required()
    def get(self):
        '''Listar todas los Games Articles'''
        controller = GameArticlesController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear un Game Articles'''
        form = request_schema.create().parse_args()
        controller = GameArticlesController()
        return controller.create(form)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class GameArticlesById(Resource):
    @jwt_required()
    def get(self, id):
        '''Obtener un Game Articles por el ID'''
        controller = GameArticlesController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar un Game Articles por el ID'''
        form = request_schema.update().parse_args()
        controller = GameArticlesController()
        return controller.update(id, form)

    @jwt_required()
    def delete(self, id):
        '''Desabilitar un Game Articles por el ID'''
        controller = GameArticlesController()
        return controller.delete(id)


api.add_namespace(namespace)
