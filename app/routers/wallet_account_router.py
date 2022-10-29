from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.schemas.wallet_account_schema import WalletAccountRequestSchema
from app.controllers.wallet_account_controller import WalletAccountController

namespace = api.namespace(
    name='Cuenta de la Billetera',
    description='Endpoints para la Wallet Account',
    path='/wallet_account'
)

request_schema = WalletAccountRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class WalletAccount(Resource):
    @jwt_required()
    def get(self):
        '''Listar todas las Wallet'''
        controller = WalletAccountController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear una Wallet'''
        controller = WalletAccountController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class WalletAccount(Resource):
    @jwt_required()
    def get(self, id):
        '''Obtener una Wallet por el ID'''
        controller = WalletAccountController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar una Wallet por el ID'''
        controller = WalletAccountController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        '''Desabilitar una Wallet por el ID'''
        controller = WalletAccountController()
        return controller.delete(id)


api.add_namespace(namespace)
