from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required, current_user
from app.schemas.shopping_cart_schema import ShoppingCartsRequestSchema
from app.controllers.shopping_cart_controller import ShoppingCartsController

namespace = api.namespace(
    name='Carrito de compras',
    description='Endpoints para traer el carrito de compras',
    path='/shopping_cart'
)

request_schema = ShoppingCartsRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class ShoppingCart(Resource):
    @jwt_required()
    def get(self):
        '''Listar un Items del Carrito'''
        controller = ShoppingCartsController()
        return controller.all()

    @jwt_required()
    @namespace.expect(request_schema.update(), validate=True)
    def put(self):
        '''Crear o Actializar un Juegos del Carrito'''
        controller = ShoppingCartsController()
        return controller.update(request.json)
    


@namespace.route('/<int:item_id>')
@namespace.doc(security='Bearer')
class ShoppingCartById(Resource):

    @jwt_required()
    def delete(self, item_id):
        '''Eliminar un Item del Carrito por el ID'''
        controller = ShoppingCartsController()
        return controller.delete(item_id)


api.add_namespace(namespace)
