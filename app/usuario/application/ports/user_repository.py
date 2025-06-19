from abc import ABC, abstractmethod


from app.usuario.domain.user import User


class IUserRepository(ABC):
    @abstractmethod
    async def find_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass
