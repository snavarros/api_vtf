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

    async def create(self, user: User) -> User:
        self.session.add(User)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def update(self, user: User) -> User:
        await self.db.commit()
        await self.db.refresh(user)
        return user
