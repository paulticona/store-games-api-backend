from app import db
from app.models.wallet_model import WalletModel
from app.schemas.wallet_schema import WalletResponseSchema
from flask_jwt_extended import current_user

class WalletController:
    def __init__(self):
        self.model = WalletModel
        self.schema = WalletResponseSchema
        self.user_id = current_user['id']

    def all(self):
        try:
            # records = self.model.where(status=True).order_by('id').all()
            # response = self.schema(many=True)
            records = self.model.where(user_id=self.user_id).order_by('id').all()
            response = self.schema(many=True)
            data = response.dump(records)

            return {
                'data': data
            }
        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def getById(self, id):
        try:
            if record := self.model.where(id=id).first():
                response = self.schema(many=False)
                return {
                    'data': response.dump(record),
                }, 200

            return {
                'message': 'NO se encontro la Wallet mencionada'
            }, 404

        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:

            # key=valuye key=value1 ...key=valuen
            new_record = self.model.create(**data)
            # * agregamos la data a la DB mediente la conneccion
            db.session.add(new_record)
            db.session.commit()

            response = self.schema(many=False)
            return {
                'message': 'La Wallet se creo con exito',
                'data': response.dump(new_record)
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def update(self, id, data):
        try:
            #! 1:26 video
            # UPDATE roles SET field=value WHERE id = ?
            if record := self.model.where(id=id).first():
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'message': 'La Wallet de actulizo con exito',
                    'data': response.dump(record),
                }, 200

            return {
                'message': 'NO se encontro la Wallet mecionada'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def delete(self, id):
        try:
            if record := self.model.where(id=id).first():

                if record.status:
                    record.update(status=False)
                    db.session.add(record)
                    db.session.commit()
                return {
                    'message': 'Se desabilito la Wallet con exito'
                }

        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500
