# -*- coding:utf-8 -*-

from . import user

@user.route('/')
def user():
    return 'user'