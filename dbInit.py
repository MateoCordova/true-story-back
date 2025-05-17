"""
from beanie import init_beanie
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from dbconn import db
from models import *

asyncio.run(init_beanie(
        database=db,
        document_models=[User, Post],
    ))"""