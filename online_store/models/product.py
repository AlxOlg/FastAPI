from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    title: str = Field(..., title='title', max_length=100)
    description: str = Field(default='', title='description', max_length=300)
    price: float = Field(..., title='price', gt=0, le=10_000_000)


class Product(BaseModel):
    prod_id: int
    title: str = Field(..., title='title', max_length=100)
    description: str = Field(default='', title='description', max_length=300)
    price: float = Field(..., title='price', gt=0, le=10_000_000)
