from ._api import api
from .dog import api as dog_api
from .user_api import ns as user_api
from .order_api import ns as order_api
from .book_api import ns as book_api

api.add_namespace(dog_api)
api.add_namespace(user_api)
api.add_namespace(book_api)
api.add_namespace(order_api)