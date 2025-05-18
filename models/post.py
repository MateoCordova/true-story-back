from beanie import Document
from . import User, Image, Video, GeoPoint
from datetime import datetime
from typing import Optional, Union, Tuple, List

class Post(Document):
    created_by: User
    created_at: datetime
    media: Union[Image, Video]
    categoria: str
    etiquetas: List[str] | None
    georeference: GeoPoint
    titulo: str

    class Settings:
        name = "posts"  # Nombre de la colección