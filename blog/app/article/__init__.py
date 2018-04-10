# -*- coding:utf-8 -*-

from flask import Blueprint

article = Blueprint(
    'article',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views