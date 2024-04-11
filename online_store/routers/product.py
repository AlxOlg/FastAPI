from typing import List
from fastapi import APIRouter

from db import products, database
from models.product import Product, ProductIn


router = APIRouter()


@router.post('/products/', response_model=Product)
async def create_product(product: ProductIn):
    """Создать товар"""
    query = products.insert().values(**product.model_dump())
    last_record_id = await database.execute(query)
    return {**product.model_dump(), 'id': last_record_id}


@router.get("/products/", response_model=List[Product])
async def read_products():
    """Получить список товаров"""
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{prod_id}", response_model=Product)
async def read_product(prod_id: int):
    """Получить данные товара"""
    query = products.select().where(products.c.prod_id == prod_id)
    return await database.fetch_one(query)


@router.put("/products/{prod_id}", response_model=Product)
async def update_product(prod_id: int, new_product: ProductIn):
    """Обновить данные товара"""
    query = products.update().where(products.c.prod_id == prod_id).values(**new_product.model_dump())
    await database.execute(query)
    return {**new_product.model_dump(), "prod_id": prod_id}


@router.delete("/products/{prod_id}")
async def delete_product(prod_id: int):
    """Удалить товар"""
    query = products.delete().where(products.c.prod_id == prod_id)
    await database.execute(query)
    return {'Product deleted': f"ID удаленного продукта = {prod_id}"}
