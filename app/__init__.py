

from os import getenv
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_env

## ? INSTANCIAS
# *instancia de flask Flask
app = Flask(__name__)
# * adjuntamos la confirguracion de config.py
app.config.from_object(config_env[getenv('FLASK_ENV')])

# *instancia de flask-restx Api
# y le pasamos como parametro las instacia de de flask
api = Api(app)

# *instancia de flask-sqlalchemy SQLAlchemy
db = SQLAlchemy(app)

# *instancia de flask_migrate migrate
migrate = Migrate(app, db)