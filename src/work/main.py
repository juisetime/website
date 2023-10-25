from sqlalchemy import Column, Integer, String, REAL

from src.Models import Base


class WorkModel(Base):
    __tablename__ = 'work'

    id = Column(Integer, primary_key=True, index=True)
    salary = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    datetosalaryM = Column(REAL)
    datetolevelupM = Column(Integer)

