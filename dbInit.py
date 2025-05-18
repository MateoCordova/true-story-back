
from beanie import init_beanie
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from db import db
from models import User, Post, Image, GeoPoint
from random import random, choice, sample, uniform
from datetime import datetime, timezone
import base64
from pymongo import GEOSPHERE

SAMPLE_IMAGE_BASE64 = base64.b64encode(b"fake-image-bytes").decode("utf-8")

lugares = {
    "KrugerCorp":(-0.185154, -78.474481),
    "Granados":(-0.166208, -78.469182),
    "SimonBolivar":(-0.170558, -78.452818),
    "CentroExposicionesQuito":(-0.181601, -78.486632)
}

async def create_users():
    users = [
        User(username="cryptoHacker", walletAddress="0xAAA", profilepic=None),
        User(username="bob", walletAddress="0xBBB", profilepic=None),
        User(username="twilightSparkle", walletAddress="0xCCC", profilepic=None),
    ]
    await User.insert_many(users)
    return users

async def create_posts(users):
    posts = [
        Post(
            created_by=users[0],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_1.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["ecuador", "ejido"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 1 en El Ejido",
            categoria="Movilidad",
            destacado=False,
        ),
        Post(
            created_by=users[1],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_2.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["urbano", "mariscal"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 2 en La Mariscal",
            categoria="Cultural",
            destacado=False,
        ),
        Post(
            created_by=users[2],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_3.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["parque", "carolina"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 3 en La Carolina",
            categoria="Ocio",
            destacado=False,
        ),
        Post(
            created_by=users[0],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_4.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["historia", "san_roque"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 4 en San Roque",
            categoria="Cultural",
            destacado=False
        ),
        Post(
            created_by=users[1],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_5.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["ejido", "foto"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 5 en El Ejido",
            categoria="Social",
            destacado=False,
        ),
        Post(
            created_by=users[2],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_6.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["mariscal", "cultura"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 6 en La Mariscal",
            categoria="Educativo",
            destacado=False,
        ),
        Post(
            created_by=users[0],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_7.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["carolina", "vista"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 7 en La Carolina",
            categoria="Deportivo",
            destacado=False,
        ),
        Post(
            created_by=users[1],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_8.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["mercado", "san_roque"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 8 en San Roque",
            categoria="Ofertas",
            destacado=False,
        ),
        Post(
            created_by=users[2],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_9.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["ejido", "día"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 9 en El Ejido",
            categoria="Tránsito",
            destacado=False,
        ),
        Post(
            created_by=users[0],
            created_at=datetime.now(timezone.utc),
            media=Image(filename="foto_10.png", mime_type="image/png", data_base64=SAMPLE_IMAGE_BASE64),
            etiquetas=["mariscal", "mural"],
            georeference=GeoPoint(coordinates=lugares["Granados"]),
            titulo="Post 10 en La Mariscal",
            categoria="Cultural",
            destacado=False,
        )
    ]

    await Post.insert_many(posts)



async def seed():
    await init_beanie(database=db, document_models=[User, Post])
    print("📦 Inicializando base de datos...")

    await User.delete_all()
    await Post.delete_all()

    print("👥 Creando usuarios...")
    users = await create_users()

    print("📝 Creando posts...")
    await create_posts(users)

    print("✅ Datos de prueba insertados con éxito.")
    await db["posts"].create_index([("georeference", GEOSPHERE)])



if __name__ == "__main__":
    asyncio.run(seed())
    