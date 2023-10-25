from fastapi import APIRouter
from sqlalchemy import delete, update, insert


from src.auth.hash import *
from src.user.main import UserModel
from src.work.main import WorkModel
from src.role.main import RoleModel
from src.role.schemas import RoleCreate, RoleUpdate
from src.work.schemas import WorkCreate, WorkUpdate
from src.user.schemas import *
from typing import Annotated
from src.bases.database import *
import json
SUrouter = APIRouter(prefix='/superuser',
                   tags=['superuser'],
                   )

@SUrouter.patch(path="/addrole", description='give somebody role, only for **superuser**!!!!')
def add_role(roleid, userid, current_user: Annotated[UserRead,Depends(get_current_user)]):
    session = get_session()
    stmt = update(UserModel).where(UserModel.id == userid).values(role_id=roleid)
    session.execute(stmt)
    session.commit()



@SUrouter.post(path='/viewdata_all',description='only for **superuser**!!!!')
def view_data(current_user: Annotated[UserRead,Depends(get_current_user)]):
    sesion = get_session()
    query = select(RoleModel)
    result = sesion.execute(query)
    get: RoleModel = result.scalars().all()
    stored_data: dict = jsonable_encoder(get)

    query = select(UserModel)
    result = sesion.execute(query)
    get: UserModel = result.scalars().all()
    stored_data2: dict = jsonable_encoder(get)

    query = select(WorkModel)
    result = sesion.execute(query)
    get: WorkModel = result.scalars().all()
    stored_data3: dict = jsonable_encoder(get)


    return '*******role*******', stored_data, '******user******', stored_data2, '*******work*******', stored_data3






