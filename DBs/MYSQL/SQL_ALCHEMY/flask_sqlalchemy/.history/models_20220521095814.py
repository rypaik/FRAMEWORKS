from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from .database import Base

# MODELS FILES CREATES SCHEMA for
# table Records in DB

# TODO: find a reference for SQLAlchemy Schema Data Options
class Record(Base):
    __tablename = 'Records'
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    country = Column(String, index=True)
    cases = Column(Integer)
    deaths = Column(Integer)
    recoveries = Column(Integer)

    




