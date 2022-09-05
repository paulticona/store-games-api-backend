from flask import Flask
from flask_restx import Api

# instanciar flask
app = Flask(__name__)
# instanciamos flask-restx Api
# y le pasamos como parametro las instacia de de flask
api = Api(app)                          
