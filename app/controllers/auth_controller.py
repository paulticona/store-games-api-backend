
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from secrets import token_hex
from app import db
from app.utils.mailing import Mailing

class AuthController:
    def __init__(self):
        self.model = UserModel
        self.schemas = ''
        self.mailing = Mailing()
    def signIn(self, data): 
        try:
            # ? logeode usuarios
            # Buscar el usuario username
            if record:= self.model.where(
                    username=data.get('username'),
                    status=True    
            ).first():
                if record.checkPassword(data.get('password')):
                    access_token = create_access_token(
                        identity=record.id
                    )
                    refresh_token = create_refresh_token(
                        identity=record.id
                    )
                    return {
                        'access_token': access_token,
                        'refresh_token': refresh_token   
                    }, 200
                else:
                    raise Exception('password Invalid')

            raise Exception("No se encontro el usuario")
        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500
    def refreshToken(self, identity):
        try:
            access_token = create_access_token(
                identity=identity
            )
            return {
                'access_token': access_token
            }, 200 
        except Exception as e:
           return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500
    
    def resetPassword(self, data):
        try:
            if record := self.model.where(email=data.get('email'), status=True).first():
                new_password = token_hex(5)
                record.password = new_password
                #record.update(password=new_password)
                record.hashPassword()
                username = record.username
                self.mailing.emailResetPassword(record.email, new_password, username) 

                db.session.add(record)
                db.session.commit()
                return{
                    'message': 'Password changed successfully'
                }, 200 
            raise Exception('No se encontro el usuario')
        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500
    