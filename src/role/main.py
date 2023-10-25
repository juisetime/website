from sqlalchemy import Column, Integer, String, REAL

from src.Models import Base


class RoleModel(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    ischangedata = Column(Integer, nullable=False)
    iscreatework = Column(Integer, nullable=False)
    isusewebsite = Column(Integer, nullable=False)

