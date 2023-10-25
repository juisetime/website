from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import delete, update
from fastapi import APIRouter
from typing import Annotated
from src.auth.hash import *
from src.bases.database import *

from src.user.main import UserModel
from src.work.main import WorkModel

Urouter = APIRouter(prefix='/common',
                   tags=['everybody'],
                   )



@Urouter.post(path='/register')
def register(nickname,password):
    hashpassword = hash_password(password)
    sesion = get_session()
    query = select(UserModel)
    result = sesion.execute(query)

    get: UserModel = result.scalars().all()
    stored_data: dict = jsonable_encoder(get)
    # if len(nickname) < 3 or len(password) < 3:
    #     print('Your nickname or Password wrong')
    #
    for i in stored_data:
        if i['nickname'] == nickname:
            return "nickname can't be the same"



    stmt = insert(UserModel).values(password=hashpassword, nickname=nickname)
    # query - используется для получения информация из БД

    sesion.execute(stmt)
    sesion.commit()



    return 'you register'






@Urouter.post(path='/info/yourself')
def info(current_user: Annotated[UserRead,Depends(get_current_user)]):
    return current_user

@Urouter.patch(path="/addwork", description='податься на работу')
def add_work(workid, current_user: Annotated[UserRead,Depends(get_current_user)]):

    stmt = update(UserModel).where(UserModel.id == current_user).values(work_id=workid)
    session = get_session()
    session.execute(stmt)
    session.commit()
    return 0
