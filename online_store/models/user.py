from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    firstname: str = Field(..., title='first name', max_length=50)
    lastname: str = Field(..., title='last name', max_length=50)
    email: EmailStr = Field(..., title='emai', max_length=100)
    password: str = Field(..., title='password', min_length=4, max_length=20)


class User(BaseModel):
    user_id: int
    firstname: str = Field(..., title='first name', max_length=50)
    lastname: str = Field(..., title='last name', max_length=50)
    email: EmailStr = Field(..., title='emai', max_length=100)
