from sqlalchemy import Column, Integer, String, REAL
from src.Models import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    role_id = Column(Integer)
    work_id = Column(Integer)


