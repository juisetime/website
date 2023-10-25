from fastapi import APIRouter,Depends
from sqlalchemy import delete, update, insert
from src.user.main import UserModel
from src.work.main import WorkModel
from src.role.main import RoleModel
from src.role.schemas import RoleCreate, RoleUpdate
from src.work.schemas import WorkCreate, WorkUpdate
from src.user.schemas import *
from src.bases.database import *
from typing import Annotated
from src.auth.hash import get_current_user
WorkRouter = APIRouter(prefix='/work',
                   tags=['work']
                   )

@WorkRouter.post(path="/create", description='создать work "только для админа"')
def create_work(job: WorkCreate, current_user: Annotated[UserRead,Depends(get_current_user)]):
    # Забираем запись в work
    # stmt - используется для добавления инф. в БД
    stmt = insert(WorkModel).values(salary=job.salary,
                                    title=job.title,
                                    description=job.description,
                                    datetolevelupM=job.datetolevelupM,
                                    datetosalaryM=job.datetosalaryM)
    # query - используется для получения информация из БД
    sesion = get_session()
    sesion.execute(stmt)
    sesion.commit()
    query = select(WorkModel)
    result = sesion.execute(query)
    getwork: WorkModel = result.scalars().all()
    stored_data: dict = jsonable_encoder(getwork)
    print(stored_data)


# удаляет таблицу в user
@WorkRouter.delete(path="/delete", description='удалить work "только для админа"')
def delete_work(workid, current_user: Annotated[UserRead,Depends(get_current_user)]):
    session = get_session()
    stmt = delete(WorkModel).where(WorkModel.id == workid)
    session.execute(stmt)
    session.commit()


# удаляет таблицу в user
@WorkRouter.patch(path="/update", description='обновить work "только для админа"')
def update_work(job: WorkUpdate, workid, current_user: Annotated[UserRead,Depends(get_current_user)]):
    stmt = update(WorkModel).where(WorkModel.id == workid).values(salary=job.salary,
                                                                  title=job.title,
                                                                  description=job.description,
                                                                  datetolevelupM=job.datetolevelupM,
                                                                  datetosalaryM=job.datetosalaryM)
    session = get_session()
    session.execute(stmt)
    session.commit()