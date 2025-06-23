from fastapi import APIRouter, Depends, HTTPException, status


from app.auth.application.use_cases.authenticate_user import AuthenticateUser
from app.auth.interface_adapters.dtos.auth_dto import AuthRequestDTO
from app.auth.interface_adapters.dtos.auth_response_dto import AuthResponseDTO
from app.auth.interface_adapters.presenters.auth_presenter import AuthPresenter
from app.auth.interface_adapters.dependencies.auth import (
    get_authenticate_user,
    get_user_use_cases,
)
from app.user.application.use_cases.user_use_cases import UserUseCases
from app.user.interface_adapters.dtos.user import UserCreate


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=AuthResponseDTO)
async def login(
    credentials: AuthRequestDTO,
    use_case: AuthenticateUser = Depends(get_authenticate_user),
):
    token = await use_case.authenticate(credentials.email, credentials.password)
    return AuthPresenter.present_token(token)


@router.post("/register")
async def register_user(
    user_data: UserCreate,
    use_case: UserUseCases = Depends(get_user_use_cases),
):
    try:
        user = await use_case.create_user(user_data)
        return {"email": user.email, "message": "User created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
