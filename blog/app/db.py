# -*- coding:utf-8 -*-
from pymongo import MongoClient
from pymysql import connect
from instance.config import MONGO_URI, MYSQL_URI

def get_mongo_connection():
    """mongo数据库连接"""
    return MongoClient(host=MONGO_URI)

def get_mysql_connection():
    """Mysql数据库连接"""
    return connect(host=MYSQL_URI)

# client = pymongo.MongoClient('localhost', 27017)
# user_db = client['myblog']['users']
