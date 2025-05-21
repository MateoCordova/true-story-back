
from beanie import init_beanie
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from db import db
from models import User, Post, Image, GeoPoint, Media
from random import random, choice, sample, uniform
from datetime import datetime, timezone
import base64
from pymongo import GEOSPHERE
import os
import mimetypes
from io import BytesIO

# Ruta a la carpeta con las imágenes
folder_path = "images"

# Compression settings
JPEG_QUALITY = 60  # from 1 (worst) to 95 (best)
MAX_WIDTH = 800     # Resize if wider than this

images_data = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        # Detectar el MIME type
        mime_type, _ = mimetypes.guess_type(file_path)
        
        # Leer y codificar en base64
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            images_data.append((filename, mime_type, encoded_string))


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
            etiquetas=["Urgente", "Accidente"],
            georeference=GeoPoint(coordinates=lugares["1"]),
            titulo="Accidente en Guayabamba",
            categoria="Movilidad",
            destacado=False,
        ),
        Post(
            created_by=users[1],
            created_at=datetime.now(timezone.utc),
            etiquetas=["comida", "asado", "internacional"],
            georeference=GeoPoint(coordinates=lugares["2"]),
            titulo="Locos por el asado",
            categoria="Cultural",
            destacado=False,
        ),
        Post(
            created_by=users[2],
            created_at=datetime.now(timezone.utc),
            etiquetas=["Primax", "Asalto"],
            georeference=GeoPoint(coordinates=lugares["3"]),
            titulo="Asato en Primax Norte",
            categoria="Seguridad",
            destacado=False,
        ),
        Post(
            created_by=users[0],
            created_at=datetime.now(timezone.utc),
            etiquetas=["Vias", "Invierno"],
            georeference=GeoPoint(coordinates=lugares["4"]),
            titulo="Bache Grande en Diego de Almagro",
            categoria="Cultural",
            destacado=False
        ),
        Post(
            created_by=users[1],
            created_at=datetime.now(timezone.utc),
            etiquetas=["musica", "concierto"],
            georeference=GeoPoint(coordinates=lugares["5"]),
            titulo="Coldplay Inmersivo",
            categoria="Cultural",
            destacado=False,
        ),
        Post(
            created_by=users[2],
            created_at=datetime.now(timezone.utc),
            etiquetas=["Vías"],
            georeference=GeoPoint(coordinates=lugares["6"]),
            titulo="Bache",
            categoria="Movilidad",
            destacado=False,
        ),
        Post(
            created_by=users[0],
            created_at=datetime.now(timezone.utc),
            etiquetas=["feminismo", "emprendimiento"],
            georeference=GeoPoint(coordinates=lugares["7"]),
            titulo="Conferencia Exponencialmente Conciente",
            categoria="Cultural",
            destacado=False,
        ),
        Post(
            created_by=users[1],
            created_at=datetime.now(timezone.utc),
            etiquetas=["teatro", "CCi"],
            georeference=GeoPoint(coordinates=lugares["8"]),
            titulo="Terapia Integral",
            categoria="Cultural",
            destacado=False,
        ),
        Post(
            created_by=users[2],
            created_at=datetime.now(timezone.utc),
            etiquetas=["tecnología", "emprendimiento"],
            georeference=GeoPoint(coordinates=lugares["9"]),
            titulo="Cultural",
            categoria="Tránsito",
            destacado=False,
        ),
        Post(
            created_by=users[0],
            created_at=datetime.now(timezone.utc),
            etiquetas=["anime", "k-pop"],
            georeference=GeoPoint(coordinates=lugares["10"]),
            titulo="Budokan",
            categoria="Cultural",
            destacado=False,
        )
    ]
    medias = [
            Media(post=posts[0],media=Image(filename=images_data[0][0], mime_type=images_data[0][1], data_base64=images_data[0][2])),
            Media(post=posts[1],media=Image(filename=images_data[1][0], mime_type=images_data[1][1], data_base64=images_data[1][2])),
            Media(post=posts[2],media=Image(filename=images_data[2][0], mime_type=images_data[2][1], data_base64=images_data[2][2])),
            Media(post=posts[3],media=Image(filename=images_data[3][0], mime_type=images_data[3][1], data_base64=images_data[3][2])),
            Media(post=posts[4],media=Image(filename=images_data[4][0], mime_type=images_data[4][1], data_base64=images_data[4][2])),
            Media(post=posts[5],media=Image(filename=images_data[5][0], mime_type=images_data[5][1], data_base64=images_data[5][2])),
            Media(post=posts[6],media=Image(filename=images_data[6][0], mime_type=images_data[6][1], data_base64=images_data[6][2])),
            Media(post=posts[7],media=Image(filename=images_data[7][0], mime_type=images_data[7][1], data_base64=images_data[7][2])),
            Media(post=posts[8],media=Image(filename=images_data[8][0], mime_type=images_data[8][1], data_base64=images_data[8][2])),
            Media(post=posts[9],media=Image(filename=images_data[9][0], mime_type=images_data[9][1], data_base64=images_data[9][2])),
    ]


    await Post.insert_many(posts)
    await Media.insert_many(medias)



async def seed():
    await init_beanie(database=db, document_models=[User, Post, Media])
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
    