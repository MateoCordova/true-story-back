import uvicorn
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, Union, Tuple, List
import requests
import os
from dotenv import load_dotenv
from db import db
from session import *
from models import VerificationRequest , AuthRequest, User, Post
import asyncio
from beanie import init_beanie
from fastapi.middleware.cors import CORSMiddleware
from pymongo import GEOSPHERE


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

app = FastAPI()

# Obtiene la API Key desde variables de entorno
WORLD_ID_API_KEY = os.getenv("WORLD_ID_API_KEY")

ConnectionString = os.getenv("mongoDB")

# URL del endpoint de verificación de World ID
WORLD_ID_VERIFY_URL = "https://developer.worldcoin.org/api/v2/verify/"+str(WORLD_ID_API_KEY)

@app.post("/verify-world-id")
async def verify_world_id(data: VerificationRequest):
    headers = {
        "Authorization": f"Bearer {WORLD_ID_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "merkle_root": data.merkle_root,
        "nullifier_hash": data.nullifier_hash,
        "proof": data.proof,
        "verification_level": data.credential_type,
        "action": data.action,
        "signal": data.signal
    }

    try:
        response = requests.post(WORLD_ID_VERIFY_URL, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": "verified", "data": response.json()}

@app.get("/")
def hello():
    return "Hola mundo v5"

@app.get("/ping-mongo")
async def ping_mongo():
    try:
        await db.command("ping")
        return {"status": "Mongo conectado"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/nonce")
def get_nonce():
    nonce = generate_nonce()
    nonces_store[nonce] = time.time()
    return {"nonce": nonce}

@app.post("/auth")
def auth(data : AuthRequest):
    validateNounce(data.nonce)
    newdict = {
        "username":data.username,
        "walletAddress":data.walletAddress,
        "profilepic":data.profilePictureUrl,
        "exp":""
        }
    #guardar usr en database
    access_token = create_access_token(data=newdict)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/posts/cercanos", response_model=List[Post])
async def obtener_posts_cercanos(
    lat: float = Query(..., description="Latitud"),
    lon: float = Query(..., description="Longitud"),
    max_results: int = 10
):
    await init_beanie(database=db,document_models=[User, Post])
    pipeline = [
        {
            "$geoNear": {
                "near": {"type": "Point", "coordinates": [lon, lat]},
                "distanceField": "distancia",
                "spherical": True
            }
        },
        {
            "$limit": max_results
        }
    ]

    # Ejecutar la agregación sobre la colección
    cursor = db["posts"].aggregate(pipeline)
    results = []
    async for doc in cursor:
        results.append(Post(**doc))  # reconstruye como objetos Beanie
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    