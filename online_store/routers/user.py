from typing import List
from fastapi import APIRouter

from db import users, database
from models.user import User, UserIn


router = APIRouter()


@router.post('/users/', response_model=User)
async def create_user(user: UserIn):
    """Создать пользователя"""
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), 'id': last_record_id}


@router.get("/users/", response_model=List[User])
async def read_users():
    """Получить список пользователей"""
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    """Получить данные пользователя"""
    query = users.select().where(users.c.user_id == user_id)
    return await database.fetch_one(query)


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    """Обновить данные пользователя"""
    query = users.update().where(users.c.user_id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), "user_id": user_id}


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Удалить пользователя"""
    query = users.delete().where(users.c.user_id == user_id)
    await database.execute(query)
    return {'User deleted': f"ID удаленного пользователя = {user_id}"}
