from beanie import Document
from typing import Optional, Union, Tuple, List
class User(Document):  # Inherit from Document, not BaseModel
    username: str
    walletAddress: str
    profilepic: Optional[str]

    class Settings:
        name = "users"  # Nombre de la colección