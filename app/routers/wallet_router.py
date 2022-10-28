from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.schemas.wallet_schema import WalletRequestSchema
from app.controllers.wallet_controller import WalletController

namespace = api.namespace(
    name='Wallet',
    description='Endpoints para la Wallet',
    path='/wallet'
)

request_schema = WalletRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Wallet(Resource):
    @jwt_required()
    def get(self):
        '''Listar todas las Wallet'''
        controller = WalletController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear una Wallet'''
        controller = WalletController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class WalletById(Resource):
    @jwt_required()
    def get(self, id):
        '''Obtener una Wallet por el ID'''
        controller = WalletController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar una Wallet por el ID'''
        controller = WalletController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        '''Desabilitar una Wallet por el ID'''
        controller = WalletController()
        return controller.delete(id)


api.add_namespace(namespace)
