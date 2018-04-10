# -*- coding:utf-8 -*-

from . import article

@article.route('/')
def article():
    return 'article'