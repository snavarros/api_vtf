from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated, Optional


class UserCreate(BaseModel):
    name: str | None
    lastName: Optional[str]
    email: EmailStr
    hashed_password: Annotated[
        str,
        StringConstraints(min_length=8),
    ]
    phone: Optional[str]
    region: int
    role: Optional[str] = "default"
    is_admin: Optional[bool] = False
    is_active: Optional[bool] = False
    provider: Optional[str] = "local"


class UserUpdate(BaseModel):
    name: Optional[str]
    lastName: Optional[str]
    hashed_password: Annotated[
        str,
        StringConstraints(min_length=8),
    ]
    phone: Optional[str]
    region: Optional[int]
    role: Optional[str]
    is_admin: Optional[bool]
    is_active: Optional[bool]
    provider: Optional[str]
