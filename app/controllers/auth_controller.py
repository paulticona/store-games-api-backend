
from app.models.users_model import UserModel

class AuthController:
    def __init__(self):
        self.model = UserModel
        self.schemas = ''
    def signIn(self, data): 
        try:
            # ? logeode usuarios
            # Buscar el usuario username
            if record:= self.model.where(
                    username=data.get('username'),
                    status=True    
            ).first():
                if record.checkPassword(data.get('password')):
                    return {
                        'message': 'success'
                    }
                else:
                    raise Exception('password Invalid')

            raise Exception("No se encontro el usuario")
        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500