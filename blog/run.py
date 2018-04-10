# -*- coding:utf-8 -*-
from app import app

app.config.from_object('config')

if __name__ == '__main__':
    app.run()