import pytest
from unittest.mock import AsyncMock
from jose import jwt

from app.auth.interface_adapters.api.dependencies.auth import get_current_user
from app.config.settings import settings
from app.usuario.domain.user import User


@pytest.mark.asyncio
async def test_get_current_user_success():
    # Arrange
    email = "user@example.com"
    token = jwt.encode({"sub": email}, settings.SECRET_KEY, algorithm="HS256")

    fake_user = User(
        name="John",
        lastName="Doe",
        email=email,
        hashed_password="hashed_pwd",
        region=1,
        phone="5691234567",
    )

    mock_repo = AsyncMock()
    mock_repo.find_by_email.return_value = fake_user

    # Act
    user = await get_current_user(token=token, repository=mock_repo)

    # Assert
    assert user.email == email
    mock_repo.find_by_email.assert_awaited_once_with(email)
