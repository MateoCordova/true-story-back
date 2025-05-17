import os
from pymongo import MongoClient

uri = os.getenv("mongoDB")
client = MongoClient(uri)

db = client["Hackathon"]
