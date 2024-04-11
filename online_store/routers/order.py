from typing import List
from fastapi import APIRouter

from db import orders, database
from models.order import Order, OrderIn


router = APIRouter()


@router.post('/orders/', response_model=Order)
async def create_order(order: OrderIn):
    """Создать заказ"""
    query = orders.insert().values(**order.model_dump())
    last_record_id = await database.execute(query)
    return {**order.model_dump(), 'order_id': last_record_id}


@router.get("/orders/", response_model=List[Order])
async def read_orders():
    """Получить список заказов"""
    query = orders.select()
    return await database.fetch_all(query)


@router.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    """Получить данные заказа"""
    query = orders.select().where(orders.c.order_id == order_id)
    return await database.fetch_one(query)


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    """Обновить данные заказа"""
    query = orders.update().where(orders.c.order_id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), "order_id": order_id}


@router.delete("/orders/{order_id}")
async def delete_product(order_id: int):
    """Удалить заказ"""
    query = orders.delete().where(orders.c.order_id == order_id)
    await database.execute(query)
    return {'order deleted': f"ID удаленного заказы = {order_id}"}
