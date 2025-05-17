from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Union, Tuple, List

class Image(BaseModel):
    url: str
    description: Optional[str]

class Video(BaseModel):
    url: str
    duration: Optional[float]

class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    walletAddress: str
    profilepic: str | None
    exp: str | None

class Post(BaseModel):
    created_by: User
    created_at: datetime
    media : Image | Video
    etiquetas : list[str]
    georeference : tuple[float , float]
    titulo: str

# Modelo de datos para la solicitud
class VerificationRequest(BaseModel):
    merkle_root: str
    nullifier_hash: str
    proof: str
    credential_type: str
    action: str
    signal: str

class Permission(BaseModel):
    notifications: bool
    contacts: bool


class AuthRequest(BaseModel):
    walletAddress: str | None
    username: str | None
    profilePictureUrl: str | None
    #permissions:  Optional[Permission] = None  Bug pendiente :c
    optedIntoOptionalAnalytics: bool | None
    worldAppVersion : float | None
    deviceOS: str
    nonce: str

