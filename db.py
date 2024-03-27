from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

MONGODB_URL = os.environ.get("MONGO_URI",None)
client = MongoClient(MONGODB_URL)
db = client["encryption_db"]
