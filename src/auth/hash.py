import hashlib as hash
from src.user.main import UserModel
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from src.user.schemas import UserRead

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


def hash_password(password: str):
    hashP = hash.md5(password.encode()).hexdigest()
    return hashP


def fake_decode_token(token):
    return UserRead(
        nickname=token + 'fake'
    )
# изменино удаленно юсер рид потому что не работало
