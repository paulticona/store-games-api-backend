from app import db
from app.models.users_model import UserModel
from app.schemas.users_schema import UsersResponseSchema


class UsersController:
    def __init__(self):
        self.model = UserModel
        self.schema = UsersResponseSchema

    def all(self, page, per_page):
        try:
            # Paginate
            # page -> La pagina actual
            # per_page -> total de registros por pagina
            # total -> total de registros
            # pages -> total de paginas
            # items -> Lista de objetos
            records = self.model.where(status=True).order_by('id').paginate(
                per_page=per_page, page=page
            )
            print(records.__dict__)
            response = self.schema(many=True)
            return {
                # response.dump(records)
                'resultados': response.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'per_page': records.per_page,
                    'currentpage': records.page
                }
            }

        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def getById(self, id):
        try:
           # SELECT FROM roles WHERE id = id
            if record := self.model.where(id=id).first():
                response = self.schema(many=False)
                return {
                    'data': response.dump(record),
                }, 200

            return {
                'message': 'NO se encontro el user mencionado'
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
            new_record.hashPassword()
            # * agregamos la data a la DB mediente la conneccion
            db.session.add(new_record)
            db.session.commit()
            # * serializamos el objeto
            response = self.schema(many=False)
            return {
                'message': 'el user se creo con exito',
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
                    'message': 'success para actualizar el Usuario',
                    'data': response.dump(record),
                }, 200

            return {
                'message': 'NO se encontro el usuario mencionado'
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
                    'message': 'Se desabilito el usuario con exito'
                }

        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500
