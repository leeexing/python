from flask import Blueprint
from flask_restplus import Api
from app.apis.dog import api as dog_api

# api_blueprint = Blueprint('open_api', __name__, url_prefix='/api')
# api = Api(api_blueprint, version='1.2', prefix='/v1', title='OpenApi')

api = Api(
    title='Zoo API',
    version='1.0',
    description='A simple demo API',
)
api.add_namespace(dog_api)
