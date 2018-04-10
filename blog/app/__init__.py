# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .home import home
from .article import article
from .user import user

app = Flask(__name__)
# db = SQLAlchemy(app)

# 注册蓝图
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(article, url_prefix='/article')




