from abc import ABC, abstractmethod
from datetime import timedelta


class IAuthService(ABC):
    @abstractmethod
    def get_password_hash(password: str) -> str:
        pass

    @abstractmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        pass

    @abstractmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
        pass

    @abstractmethod
    def decode_access_token(token: str):
        pass

    @abstractmethod
    def create_reset_token(email: str, expire_minutes: str):
        pass

    @abstractmethod
    def verify_reset_token(token: str):
        pass
