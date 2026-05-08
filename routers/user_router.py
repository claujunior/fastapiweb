from fastapi import APIRouter
from services.user_service import get_users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("")
async def users():
    return await get_users()