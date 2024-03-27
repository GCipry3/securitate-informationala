from pymongo import MongoClient

MONGODB_URL = "mongodb://root:rootpassword@localhost:27017/encryption_db"
client = MongoClient(MONGODB_URL)
db = client["encryption_db"]
