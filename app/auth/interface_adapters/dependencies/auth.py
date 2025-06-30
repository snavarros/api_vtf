from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from app.config.settings import settings
from app.user.application.ports.user_repository import IUserRepository


from fastapi.security import OAuth2PasswordBearer

from app.auth.application.ports.auth_service import IAuthService
from app.auth.application.use_cases.authenticate_user import AuthenticateUser
from app.config.database import get_db
from app.user.infrastructure.repositories.user_repository import UserRepository

from sqlalchemy.ext.asyncio import AsyncSession

from app.user.application.use_cases.user_use_cases import UserUseCases
from app.auth.infrastructure.services.jwt_auth_service import AuthServiceJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_user_repository(db: AsyncSession = Depends(get_db)) -> IUserRepository:
    return UserRepository(db)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    repository: IUserRepository = Depends(get_user_repository),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_email = str(payload.get("sub"))
    except (JWTError, ValueError):
        raise credentials_exception

    user = await repository.find_by_email(user_email)

    if user is None:
        raise credentials_exception

    return user


def get_auth_service() -> IAuthService:
    return AuthServiceJWT()


def get_authenticate_user(
    db: AsyncSession = Depends(get_db),
    auth_service: IAuthService = Depends(get_auth_service),
) -> AuthenticateUser:
    user_repo = UserRepository(db)
    return AuthenticateUser(user_repo, auth_service)


def get_user_use_cases(db: AsyncSession = Depends(get_db)) -> UserUseCases:
    repo = UserRepository(db)
    return UserUseCases(repo)


def get_user_repository(db: AsyncSession = Depends(get_db)) -> IUserRepository:
    return UserRepository(db)
