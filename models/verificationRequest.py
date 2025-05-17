from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Union, Tuple, List

class VerificationRequest(BaseModel):
    merkle_root: str
    nullifier_hash: str
    proof: str
    credential_type: str
    action: str
    signal: str