from os import getenv
from flask import Flask
from flask_restx import Api
from config import config_env

print(config_env[getenv('FLASK_ENV')])

# instanciar flask
app = Flask(__name__)
# * adjuntamos la confirguracion de config.py
app.config.from_object(config_env[getenv('FLASK_ENV')])
# instanciamos flask-restx Api
# y le pasamos como parametro las instacia de de flask
api = Api(app)
