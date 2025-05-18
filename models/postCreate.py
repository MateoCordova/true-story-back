from pydantic import BaseModel
from typing import List, Union
from datetime import datetime
from models import Image, Video, GeoPoint

class PostCreate(BaseModel):
    media: Union[Image, Video]
    etiquetas: List[str] | None
    georeference: GeoPoint
    titulo: str
    categoria: str

