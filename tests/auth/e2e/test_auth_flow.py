import pytest
from httpx import AsyncClient
from main import app
from fastapi import status


@pytest.mark.asyncio
async def test_auth_flow(override_get_db):
    async with AsyncClient(app=app, base_url="http://test") as client:
        # 1. Registro de usuario
        user_data = {
            "email": "testuser@example.com",
            "password": "Test1234!",
            "name": "Test",
            "lastName": "User",
            "region": 1,
        }

        response = await client.post("/auth/register", json=user_data)
        assert response.status_code == status.HTTP_201_CREATED
        created = response.json()
        assert created["email"] == user_data["email"]

        # 2. Login
        login_data = {
            "username": user_data["email"],
            "password": user_data["password"],
        }

        response = await client.post("/auth/login", data=login_data)
        assert response.status_code == status.HTTP_200_OK
        json_data = response.json()
        assert "access_token" in json_data
        token = json_data["access_token"]

        # 3. Acceso a endpoint protegido
        headers = {"Authorization": f"Bearer {token}"}
        response = await client.get("/users/me", headers=headers)

        assert response.status_code == status.HTTP_200_OK
        user_info = response.json()
        assert user_info["email"] == user_data["email"]
        assert user_info["name"] == user_data["name"]
