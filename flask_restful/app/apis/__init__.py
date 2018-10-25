from .user_api import ns as user_api
# from .order_api import ns as order_api
# from .book_api import ns as book_api

from flask import Blueprint
from flask_restplus import Api
from app.apis.dog import api as dog_api
from app.apis.user_api import ns as user_api

# api_blueprint = Blueprint('open_api', __name__, url_prefix='/api')
# api = Api(api_blueprint, version='1.2', prefix='/v1', title='OpenApi')

api = Api(
    title='Douban Music API',
    version='1.0',
    description='Douban Music API for react-flask',
)
api.add_namespace(dog_api)
api.add_namespace(user_api)