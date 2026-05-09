from fastapi import HTTPException

from repositories.user_repository import find_all_users, insert_user, find_user_by_username
from model.user_model import User
from dto.user_dto import UserDTO

async def get_users():
    users = await find_all_users()
    response = []

    for user in users:
         response.append(
            UserDTO(
                username=user["username"]
            )
        )
    return response


async def create_user(user: User):

    existing_user = await find_user_by_username(
        user.username
    )
    if existing_user:
       raise HTTPException(
            status_code=400,
            detail="Usuário já existe"
       )
    
    user_dict = user.model_dump()
    user_id = await insert_user(user_dict)

    return {
        "id": user_id,
        "message": "Usuário cadastrado"
    }

