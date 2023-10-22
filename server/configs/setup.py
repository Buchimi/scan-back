from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# this function should return the mongo client
load_dotenv()
username = os.getenv("USER_ROOT_MONGODB")
password = os.getenv("PASS_ROOT_MONGODB")
uri = f"mongodb+srv://{username}:{password}@cluster0.qqwrckh.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
