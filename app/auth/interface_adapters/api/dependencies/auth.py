from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from app.config.settings import settings
from app.usuario.application.ports.user_repository import IUserRepository


from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme), repository: IUserRepository = Depends()
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
