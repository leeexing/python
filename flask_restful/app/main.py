from flask import Flask
from app.apis import api
# from app.api import api

def create_app():
    app = Flask('DEMO')
    api.init_app(app)
    return app
