from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.user.application.ports.user_repository import IUserRepository
from app.user.infrastructure.orm.models import UserORM
from app.user.domain.user import User


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            select(UserORM).where(UserORM.email == email)
        )
        return result.scalar_one_or_none()

    async def create(self, user: User):
        user_model = UserORM(
            name=user.name,
            last_name=user.last_name,
            email=user.email,
            hashed_password=user.hashed_password,
            phone=user.phone,
            region=user.region,
            role=user.role,
            is_admin=user.is_admin,
            is_active=user.is_active,
            provider=user.provider,
        )
        self.session.add(user_model)
        await self.session.commit()
        await self.session.refresh(user_model)
        return User(
            id=user_model.id,
            name=user_model.name,
            last_name=user_model.last_name,
            email=user_model.email,
            hashed_password=user_model.hashed_password,
            phone=user_model.phone,
            region=user_model.region,
            role=user_model.role,
            is_admin=user_model.is_admin,
            is_active=user_model.is_active,
            provider=user_model.provider,
        )

    async def update(self, user: User) -> User:
        await self.db.commit()
        await self.db.refresh(user)
        return user
