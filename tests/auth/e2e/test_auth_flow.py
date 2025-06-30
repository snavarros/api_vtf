import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app
from fastapi import status


@pytest.mark.asyncio
async def test_auth_flow(override_get_db):
    _ = override_get_db
    # Usar ASGITransport para probar FastAPI sin servidor externo

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # 1. Registro de usuario
        user_data = {
            "name": "Sebastián",
            "last_name": "Navarro",
            "email": "testuser@example.com",
            "hashed_password": "Test1234!",
            "phone": "+12345678",
            "region": 1,
            "role": "default",
            "is_admin": True,
            "is_active": True,
            "provider": "local",
        }

        response = await client.post("/auth/register", json=user_data)
        print("Response REGISTER:", response.json())
        assert response.status_code == status.HTTP_201_CREATED
        created = response.json()
        assert created["email"] == user_data["email"]

        # 2. Login
        login_data = {
            "email": user_data["email"],
            "password": user_data["hashed_password"],
        }

        response = await client.post("/auth/login", json=login_data)
        print("Response LOGIN:", response.json())
        assert response.status_code == status.HTTP_200_OK
        json_data = response.json()
        assert "access_token" in json_data
        token = json_data["access_token"]

        # 3. Acceso a endpoint protegido
        headers = {"Authorization": f"Bearer {token}"}
        response = await client.get("/users/me", headers=headers)
        print("Response ME:", response.json())
        assert response.status_code == status.HTTP_200_OK
        user_info = response.json()
        assert user_info["email"] == user_data["email"]
        assert user_info["name"] == user_data["name"]
