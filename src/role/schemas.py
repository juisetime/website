from typing import Optional

from pydantic import EmailStr, Field, BaseModel



# чтение
class RoleRead(BaseModel):
    id : Optional[int]
    title: Optional[str]
    ischangedata : Optional[int]
    iscreatework : Optional[int]
    isusewebsite : Optional[int]

# создание
class RoleCreate(BaseModel):
    title: str
    ischangedata: int
    iscreatework: int
    isusewebsite: int


# обновление
class RoleUpdate(BaseModel):
    title: Optional[str]
    ischangedata: Optional[int]
    iscreatework: Optional[int]
    isusewebsite: Optional[int]
