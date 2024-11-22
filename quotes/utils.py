import os
from pymongo import MongoClient
import mongoengine
from django.conf import settings


_mongo_client = None

def get_mongodb():
    mongo_name = settings.MONGODB_NAME
    global _mongo_client 
    if _mongo_client is None:  
        try:
            mongo_uri = settings.MONGODB_URI
            _mongo_client = MongoClient(mongo_uri)
            print("Connected to MongoDB")
        except Exception as e:
            print("Could not connect to MongoDB:", e)
            return None
    return _mongo_client[mongo_name]

   
db = get_mongodb()

if db is not None:
    try:
        db.command('ping')
        print("Connected to database:", db.name)
    except Exception as e:
        print("Could not connect to the database:", e)
else:
    print("Could not connect to the database: db is None")