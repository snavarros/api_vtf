from datetime import timedelta
from app.auth.application.ports.auth_service import IAuthService
from app.config import settings
from app.usuario.application.ports.user_repository import IUserRepository


class AuthenticateUser:
    def __init__(self, repository: IUserRepository, auth: IAuthService):
        self.repository = repository
        self.auth = auth

    async def authenticate(self, email: str, password: str) -> str:
        user = self.repository.find_by_email(email)
        if not user:
            raise Exception("User not found")

        if not self.auth.verify_password(password, user.hashed_password):
            raise Exception("Invalid credentials")

        token = self.auth.create_access_token(
            data={"sub": str(user.id)},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        )

        return token
