from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
import random
import string
import time

nonces_store = {}

# Clave secreta para firmar el JWT
SECRET_KEY = "Simbatelacomes"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(datetime.timezone.now) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def generate_nonce(length: int = 8) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def validateNounce(nonce: str):
    if nonce not in nonces_store:
        raise HTTPException(status_code=400, detail="Nonce inválido")
    if time.time() - nonces_store[nonce] > 300:
        del nonces_store[nonce]
        raise HTTPException(status_code=400, detail="Nonce inválido")
    del nonces_store[nonce]