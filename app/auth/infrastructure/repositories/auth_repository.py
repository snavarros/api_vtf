from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.usuario.domain.user import User


class AuthRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_email(self, email: str) -> User | None:
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def update_password(self, user: User, hashed_password: str):
        user.hashed_password = hashed_password
        self.session.add(user)
        await self.session.commit()
