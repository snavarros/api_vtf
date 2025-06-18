from pydantic import ValidationError
import pytest
from app.usuario.domain.user import User


def test_should_create_user():
    user = User(
        name="test",
        lastName="test",
        email="test@example.com",
        hashed_password="hashed123",
        region=1,
        phone="5691234567",
    )

    assert user.email == "test@example.com"


def test_should_fail_create_user_without_email():
    with pytest.raises(ValidationError):
        User(
            name="example",
            lastname="example",
            hashed_password="hashed",
            phone="+56983927982",
            is_admin=True,
            is_active=True,
            provider="local",
            region=8,
        )


def test_should_fail_create_user_with_incorrect_email():
    with pytest.raises(ValidationError):
        User(
            name="example",
            lastname="example",
            hashed_password="hashed",
            phone="+56983927982",
            is_admin=True,
            is_active=True,
            provider="local",
            region=8,
            email="example@",  # O simplemente omitirlo si lo haces opcional en la firma
        )


def test_should_fail_create_user_without_region():
    with pytest.raises(ValidationError):
        User(
            name="example",
            lastname="example",
            email="example@company.com",
            hashed_password="hashed",
            phone="+56983927982",
            is_admin=True,
            is_active=True,
            provider="local",
        )
