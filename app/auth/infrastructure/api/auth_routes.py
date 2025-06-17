from fastapi import APIRouter, Depends


from app.auth.application.use_cases.authenticate_user import AuthenticateUser
from app.auth.interface_adapters.dtos.auth_dto import AuthRequestDTO
from app.auth.interface_adapters.dtos.auth_response_dto import AuthResponseDTO
from app.auth.interface_adapters.presenters.auth_presenter import AuthPresenter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=AuthResponseDTO)
async def login(credentials: AuthRequestDTO, use_case: AuthenticateUser = Depends()):
    token = await use_case.authenticate(credentials.email, credentials.password)
    return AuthPresenter.present_token(token)
