from beanie import Document
from typing import Optional, Union, Tuple, List
from datetime import datetime


class User(Document):  # Inherit from Document, not BaseModel
    username: str
    walletAddress: str
    profilepic: Optional[str]
    exp: Optional[str]

    class Settings:
        name = "users"  # Nombre de la colección


class Post(Document):
    created_by: User
    created_at: datetime
    media: List[str]
    etiquetas: List[str]
    georeference: Tuple[float, float]
    titulo: str

    class Settings:
        name = "posts"  # Nombre de la colección
