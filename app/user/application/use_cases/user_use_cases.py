from app.user.application.ports.user_repository import IUserRepository
from app.user.domain.user import User
from app.user.interface_adapters.dtos.user import UserCreate, UserUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserUseCases:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def find_by_email(self, email: str) -> User | None:
        return await self.user_repository.find_by_email(email)

    async def create_user(self, user_data: UserCreate) -> User:
        existing = await self.user_repository.find_by_email(user_data.email)

        if existing:
            raise ValueError("User with this email already exists")

        hashed_password = pwd_context.hash(user_data.hashed_password)

        user = User(
            name=user_data.name,
            last_name=user_data.last_name,
            email=user_data.email,
            hashed_password=hashed_password,
            phone=user_data.phone,
            region=user_data.region,
            role=user_data.role,
            is_admin=user_data.is_admin,
            is_active=True,
            provider=user_data.provider,
        )

        return await self.user_repository.create(user)

    async def update_user(self, user_id: int, user_data: UserUpdate) -> User:
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise ValueError("User Not Found")

        update_data = user_data.model_dump(exclude_unset=True)

        if "password" in update_data:
            user.hashed_password = pwd_context.hash(update_data.pop("password"))

        for field, value in update_data.items():
            setattr(user, field, value)

        return await self.user_repository.update(user)
