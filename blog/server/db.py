import pymongo

client = pymongo.MongoClient('localhost', 27017)
user_db = client['myblog']['users']
