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
UserRouter = APIRouter(prefix='/user',
                   tags=['user']
                   )

# создает таблицу в user
@UserRouter.post(path="/create", description='создать user "только для админа"')
def create_user(user: UserCreate, current_user: Annotated[UserRead,Depends(get_current_user)]):
    # Забираем запись в user
    # stmt - используется для добавления инф. в БД
    stmt = insert(UserModel).values(password=user.password, nickname=user.nickname)
    # query - используется для получения информация из БД
    sesion = get_session()
    sesion.execute(stmt)
    sesion.commit()



# удаляет таблицу в user
@UserRouter.delete(path="/delete", description='удалить user "только для админа"')
def delete_user(userid, current_user: Annotated[UserRead,Depends(get_current_user)]):
    session = get_session()
    stmt = delete(UserModel).where(UserModel.id == userid)
    session.execute(stmt)
    session.commit()


# удаляет таблицу в user
@UserRouter.patch(path="/update", description='обновить user "только для админа"')
def update_user(user: UserUpdate, userid, current_user: Annotated[UserRead,Depends(get_current_user)]):
    stmt = update(UserModel).where(UserModel.id == userid).values(password=user.password, nickname=user.nickname)
    session = get_session()
    session.execute(stmt)
    session.commit()
