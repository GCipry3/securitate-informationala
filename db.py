from pymongo.mongo_client import MongoClient
import os

uri = os.getenv("MONGO_URI")
print(uri)
client = MongoClient(uri)
