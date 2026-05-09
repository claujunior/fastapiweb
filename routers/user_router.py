from fastapi import APIRouter
from services.user_service import get_users
from services.user_service import create_user
from model.user_model import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("")
async def users():
    return await get_users()

@router.post("")
async def create_users(user: User):
    return await create_user(user) 