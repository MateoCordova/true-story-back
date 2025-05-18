
from beanie import init_beanie
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from db import db
from models import User, Post, Image, GeoPoint
from random import random, choice, sample, uniform
from datetime import datetime, timezone
import base64
from pymongo import GEOSPHERE
import os

# Ruta a la carpeta con las imágenes
folder_path = "images"

# Diccionario para guardar los resultados
images_base64 = {}

# Recorremos todos los archivos en la carpeta
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Asegurarse de que sea un archivo (y no una subcarpeta, por ejemplo)
    if os.path.isfile(file_path):
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            images_base64[filename] = encoded_string


lugares = {
    "1":(-0.065627, -78.363725),
    "2":(-0.199014, -78.434874),
    "3":(-0.159903, -78.466768),
    "4":(-0.192961, -78.482850),
    "5":(-0.181316, -78.501607),
    "6":(-0.157373, -78.479745),
    "7":(-0.221672, -78.510597),
    "8":(-0.176611, -78.485639),
    "9":(-0.198576, -78.436376),
    "10":(-0.181439, -78.486586)
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
    