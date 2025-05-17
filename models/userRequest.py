from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Union, Tuple, List

class UserRequest(BaseModel):
    username: str
    walletAddress: str
    profilepic: str | None
    exp: str | None