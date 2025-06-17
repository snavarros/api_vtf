from pydantic import BaseModel


class AuthResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"
