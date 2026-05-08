from database.mongodb import db

async def find_all_users():

    users = []

    cursor = db.users.find()

    async for user in cursor:

        user["_id"] = str(user["_id"])

        users.append(user)

    return users