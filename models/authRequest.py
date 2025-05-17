from pydantic import BaseModel, Field

class Permission(BaseModel):
    notifications: bool
    contacts: bool


class AuthRequest(BaseModel):
    walletAddress: str | None
    username: str | None
    profilePictureUrl: str | None
    #permissions:  Optional[Permission] = None  Bug pendiente :c
    optedIntoOptionalAnalytics: bool | None
    worldAppVersion : float | None
    deviceOS: str
    nonce: str