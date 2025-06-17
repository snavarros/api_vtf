from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.usuario.application.ports.user_repository import IUserRepository
from app.usuario.domain.user import User


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_by_email(self, email: str) -> User | None:
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
