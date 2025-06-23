from fastapi import APIRouter, Depends

from app.auth.interface_adapters.dependencies.auth import get_current_user
from app.user.domain.user import User

router = APIRouter(prefix="/users")


@router.get("/me")
async def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user
