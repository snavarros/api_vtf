from abc import ABC, abstractmethod


from app.usuario.domain.user import User


class IUserRepository(ABC):
    @abstractmethod
    async def find_by_email(self, email: str) -> User | None:
        pass
