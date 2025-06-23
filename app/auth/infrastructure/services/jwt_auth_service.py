from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt, JWTError
from app.config.settings import settings

from app.auth.application.ports.auth_service import IAuthService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthServiceJWT(IAuthService):
    def get_password_hash(self, password) -> str:
        return pwd_context.hash(password)

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
        to_encode = data.copy()
        expire = datetime.now(tz=timezone.utc) + (
            expires_delta or timedelta(minutes=30)
        )
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def decode_access_token(token: str):
        try:
            return jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
            )
        except JWTError:
            return None

    def create_reset_token(email: str, expires_minutes: int = 15):
        expire = datetime.now(tz=timezone.utc) + timedelta(minutes=expires_minutes)
        payload = {"sub": email, "exp": expire}
        return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def verify_reset_token(token: str):
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
            )
            return payload.get("sub")
        except JWTError:
            return None
