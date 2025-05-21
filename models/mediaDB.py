from beanie import Document
from . import User, Image, Video, GeoPoint, Post
from datetime import datetime
from typing import Optional, Union, Tuple, List

class Media(Document):
    post: Post
    media: Union[Image, Video]

    class Settings:
        name = "media"  # Nombre de la colección