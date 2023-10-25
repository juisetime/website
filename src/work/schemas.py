from pydantic import EmailStr, Field, BaseModel


# чтение
class WorkRead(BaseModel):
    id: int
    salary: int
    title: str
    description: str
    datetosalaryM: float
    datetolevelupM: int


# создание
class WorkCreate(BaseModel):
    salary: int = Field(ge=12000)
    title: str = Field(min_length=3, max_length=20)
    description: str = Field(max_length=45)
    datetosalaryM: float = Field(le=10)
    datetolevelupM: int


# обновление
class WorkUpdate(BaseModel):
    salary: int = Field(ge=12000)
    title: str
    description: str
    datetosalaryM: float
    datetolevelupM: int
