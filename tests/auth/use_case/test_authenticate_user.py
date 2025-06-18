# Unit Test Authenticate User
import pytest

from unittest.mock import AsyncMock, Mock
from app.auth.application.use_cases.authenticate_user import AuthenticateUser
from datetime import timedelta
from app.usuario.domain.user import User
from app.config.settings import settings


@pytest.mark.asyncio
async def test_authenticate_success():
    # Arrange
    mock_user = User(
        name="test",
        lastName="test",
        email="test@example.com",
        hashed_password="hashed123",
        region=1,
        phone="5691234567",
    )

    mock_repository = AsyncMock()
    mock_repository.find_by_email.return_value = mock_user

    mock_auth = Mock()
    mock_auth.verify_password.return_value = True
    mock_auth.create_access_token.return_value = "fake_token"

    use_case = AuthenticateUser(repository=mock_repository, auth=mock_auth)

    # Act
    token = await use_case.authenticate("test@example.com", "plain123")

    # Assert
    assert token == "fake_token"
    mock_repository.find_by_email.assert_awaited_once_with("test@example.com")
    mock_auth.verify_password.assert_called_once_with("plain123", "hashed123")

    # Verifica valores usados en el token
    mock_auth.create_access_token.assert_called_once()
    args, kwargs = mock_auth.create_access_token.call_args
    assert kwargs["data"] == {"sub": "test@example.com"}
    assert kwargs["expires_delta"] == timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
