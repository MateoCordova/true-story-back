from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://my-node-frontend.azurewebsites.net"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

app = FastAPI()

# Obtiene la API Key desde variables de entorno
WORLD_ID_API_KEY = os.getenv("WORLD_ID_API_KEY")

# URL del endpoint de verificación de World ID
WORLD_ID_VERIFY_URL = "https://developer.worldcoin.org/api/v1/verify"

# Modelo de datos para la solicitud
class VerificationRequest(BaseModel):
    merkle_root: str
    nullifier_hash: str
    proof: str
    credential_type: str
    action: str
    signal: str

@app.post("/verify-world-id")
def verify_world_id(data: VerificationRequest):
    headers = {
        "Authorization": f"Bearer {WORLD_ID_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "merkle_root": data.merkle_root,
        "nullifier_hash": data.nullifier_hash,
        "proof": data.proof,
        "credential_type": data.credential_type,
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
    return "Hola mundo v2"