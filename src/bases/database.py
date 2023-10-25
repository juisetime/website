from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import sessionmaker



from sqlalchemy import Column, Integer, String, REAL

DATABASE_URL = "postgresql://postgres:Vovan270311@localhost/workgame"
engine = create_engine(DATABASE_URL)
session_maker = sessionmaker(engine)


def get_session():
    return session_maker()

#
# Base.metadata.drop_all(bind=engine)
# # # добавление
# Base.metadata.create_all(bind=engine)
# #
# # удаление

