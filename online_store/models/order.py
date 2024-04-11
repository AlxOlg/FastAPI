import datetime
from pydantic import BaseModel, Field


class OrderIn(BaseModel):
    prod_id: int = Field(..., title='prod_id')
    user_id: int = Field(..., title='user_id')
    date: datetime.date = Field(..., title='date')
    status: bool = Field(default=True)


class Order(BaseModel):
    order_id: int
    prod_id: int = Field(..., title='prod_id')
    user_id: int = Field(..., title='user_id')
    date: datetime.date = Field(..., title='date')
    status: bool = Field(default=True)
