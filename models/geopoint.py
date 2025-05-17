from pydantic import BaseModel, Field
from typing import Optional, Union, Tuple, List

class GeoPoint(BaseModel):
    type: str = "Point"
    coordinates: List[float]