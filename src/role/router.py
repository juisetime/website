from fastapi import APIRouter, Depends
from sqlalchemy import delete, update, insert
from typing import Annotated
from src.auth.hash import get_current_user
from src.user.main import UserModel
from src.work.main import WorkModel
from src.role.main import RoleModel
from src.role.schemas import RoleCreate, RoleUpdate
from src.work.schemas import WorkCreate, WorkUpdate
from src.user.schemas import *


from src.bases.database import *
RoleRouter = APIRouter(prefix='/role',
                   tags=['role']
                   )


# создает таблицу в role
@RoleRouter.post(path="/create", description='создать role "только для админа"')
def create_role(Role: RoleCreate, current_user: Annotated[UserRead,Depends(get_current_user)]):
    # Забираем запись в role
    # stmt - используется для добавления инф. в БД
    stmt = insert(RoleModel).values(title=Role.title, ischangedata=Role.ischangedata, iscreatework=Role.iscreatework,
                                    isusewebsite=Role.isusewebsite)
    # query - используется для получения информация из БД
    sesion = get_session()
    sesion.execute(stmt)
    sesion.commit()
    query = select(RoleModel)
    result = sesion.execute(query)
    get: RoleModel = result.scalars().all()
    stored_data: dict = jsonable_encoder(get)
    print(stored_data)


# удаляет таблицу в role
@RoleRouter.delete(path="/delete", description='удалить role "только для админа"')
def delete_role(roleid, current_user: Annotated[UserRead,Depends(get_current_user)]):
    session = get_session()
    stmt = delete(RoleModel).where(RoleModel.id == roleid)
    session.execute(stmt)
    session.commit()


# удаляет таблицу в role
@RoleRouter.patch(path="/update", description='обновить role "только для админа"')
def update_role(Role: RoleUpdate, roleid, current_user: Annotated[UserRead,Depends(get_current_user)]):
    stmt = update(RoleModel).where(RoleModel.id == roleid).values(title=Role.title, ischangedata=Role.ischangedata,
                                                                  iscreatework=Role.iscreatework,
                                                                  isusewebsite=Role.isusewebsite)
    session = get_session()
    session.execute(stmt)
    session.commit()