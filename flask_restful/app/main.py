from flask import Flask
# from app.apis import api
from app.api import api

def create_app():
    app = Flask('DEMO')

    # register_api()
    # app.register_blueprint(api_blueprint)
    api.init_app(app)

    return app

# def register_api():
#     from app.apis import user_api
#     api.add_namespace(user_api)
    # api.add_namespace(order_api)
    # api.add_namespace(book_api)
