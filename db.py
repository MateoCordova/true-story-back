import os
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from beanie import init_beanie


MONGODB_URI = os.getenv("mongoDB")

client = AsyncIOMotorClient(MONGODB_URI)
db = client["Hackathon"]


