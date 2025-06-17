from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str | None
    lastName: str | None
    email: EmailStr
    hashed_password: str
    phone: str | None
    region: int
    role: str = "default"
    is_admin: bool = False
    is_active: bool = True
    provider: str = "local"
