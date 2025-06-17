from pydantic import BaseModel, EmailStr


class AuthRequestDTO(BaseModel):
    email: EmailStr
    password: str
