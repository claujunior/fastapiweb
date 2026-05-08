from repositories.user_repository import find_all_users

async def get_users():
    return await find_all_users()