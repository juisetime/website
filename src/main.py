from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import delete, update
from fastapi import APIRouter
import hashlib as hash
from src.auth.hash import *
from src.main_routers.user import Urouter
from src.main_routers.admin import SUrouter
from src.user.router import UserRouter
from src.role.router import RoleRouter
from src.work.router import WorkRouter
from src.role.schemas import RoleCreate, RoleUpdate
from src.bases.database import *
import json
from pages.router import router
from src.user.schemas import *
from src.user.main import UserModel
from src.work.main import WorkModel
from src.role.main import RoleModel
from src.work.schemas import WorkCreate, WorkUpdate
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

login = 0
app = FastAPI(title="Password Game")

app.include_router(SUrouter)
app.include_router(UserRouter)
app.include_router(WorkRouter)
app.include_router(RoleRouter)
app.include_router(Urouter)
app.include_router(router)

@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    sesion = get_session()
    query = select(UserModel)
    result = sesion.execute(query)
    get: UserModel = result.scalars().all()
    stored_data: dict = jsonable_encoder(get)
    user = 0
    for i in stored_data:
        if i['nickname'] == form_data.username:
            user = i

    if user == 0:
        raise HTTPException(status_code=400, detail="Incorrect username")
    hashpassword = hash_password(form_data.password)
    if user['password'] != hashpassword:
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {'access_token': user['nickname'] ,'token_type': 'bearer'}




@app.get('/items/')
def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'token': token}



@app.get('/users/me')
def read_users_me(current_user : Annotated[UserRead,Depends(get_current_user)]):
    return current_user


# basedanix = base.get('tables').get('users')
# alembic upgrade head
# alembic revision --autogenerate -m "create db"

# uvicorn src.main:app --reload
