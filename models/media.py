from pydantic import BaseModel, Field
class Image(BaseModel):
    filename: str
    mime_type: str  # ejemplo: 'image/png'
    data_base64: str  # el contenido en base64

class Video(BaseModel):
    filename: str
    mime_type: str  # ejemplo: 'video/mp4'
    data_base64: str