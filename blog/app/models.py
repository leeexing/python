# -*- coding:utf-8 -*-

from . import db

class Engine(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    views = db.Column(db.Integer, default=0)