from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Union, Tuple, List

class PayVerifyRequest(BaseModel):
    transaction_id : str