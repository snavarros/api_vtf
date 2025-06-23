from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.user.domain.user import User


class AuthRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def update_password(self, user: User, hashed_password: str):
        user.hashed_password = hashed_password
        self.session.add(user)
        await self.session.commit()
