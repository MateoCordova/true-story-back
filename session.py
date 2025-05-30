from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
import random
import string
import time
import uuid

nonces_store = {}
myuuid_store = {}

# Clave secreta para firmar el JWT
SECRET_KEY = "ARCANE-MAGIC"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def generate_nonce(length: int = 8) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
    
def generate_uuid() -> str:
    myuuid = uuid.uuid4()
    myuuid = str(myuuid).replace("-","")
    return myuuid

def validateNounce(nonce: str):
    if nonce not in nonces_store:
        raise HTTPException(status_code=400, detail="Nonce inválido")
    if time.time() - nonces_store[nonce] > 300:
        del nonces_store[nonce]
        raise HTTPException(status_code=400, detail="Nonce inválido")
    del nonces_store[nonce]