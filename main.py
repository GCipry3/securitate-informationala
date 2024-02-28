from dotenv import load_dotenv
load_dotenv()
from db import client

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)