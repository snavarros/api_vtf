from app.user.domain.user import User


def user_factory(orm_user) -> User:
    if orm_user.role == "default":
        return User(orm_user.email, orm_user.role)
