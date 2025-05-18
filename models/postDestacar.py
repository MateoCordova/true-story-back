from pydantic import BaseModel
from typing import List, Union
from datetime import datetime
from models import Image, Video, GeoPoint

class PostDestacar(BaseModel):
    _id: int

