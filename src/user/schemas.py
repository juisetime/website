from typing import Optional

from pydantic import EmailStr, Field, BaseModel


# чтение
class UserRead(BaseModel):
    id: Optional[int] = None
    nickname: Optional[str]
    role_id: Optional[int] = None
    work_id: Optional[int] = None


# создание
class UserCreate(BaseModel):
    password: str = Field(min_length=8, max_length=20)
    nickname: str = Field(min_length=3, max_length=16)


# обновление
class UserUpdate(BaseModel):
    password: str = Field(min_length=8, max_length=20)
    nickname: str = Field(min_length=3, max_length=16)
    role_id: int
    work_id: int
