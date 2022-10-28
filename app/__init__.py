

from os import getenv
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_env
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS

# ? INSTANCIAS
# *instancia de flask Flask
app = Flask(__name__)
# * adjuntamos la confirguracion de config.py
app.config.from_object(config_env[getenv('FLASK_ENV')])

authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

# *instancia de flask-restx Api
# y le pasamos como parametro las instacia de d e flask
api = Api(
    app,
    title='Store Games Admin',
    version='0.0.1',
    description='EndPoints StoreGames',
    authorizations=authorizations,
    contact='paulticona264riddick@gmail.com',
    doc='/'
)

# *instancia de flask-sqlalchemy SQLAlchemy
db = SQLAlchemy(app)

# *instancia de flask_migrate migrate
migrate = Migrate(app, db)

jwt = JWTManager(app)

mail = Mail(app)

CORS(app)
