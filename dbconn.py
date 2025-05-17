import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from DB.creacionesquemas import *  

MONGODB_URI = os.getenv("mongoDB")

client = AsyncIOMotorClient(MONGODB_URI)
db = client["Hackathon"]

async def initiate_database():
    await init_beanie(
        database=db,
        document_models=[User, Post],
    )