from sqlalchemy import Column, Integer, String
from sqlalchemy. types import Date
from . database import Base
class Record (Base):
    __tablename_ = "Records"
    
    id = Column (Integer, primary_key=True, index=True)
    date = Column (Date)
    country = Column (String, index=True)
    cases = Column (Integer)
    deaths = Column (Integer)
    recoveries = Column (Integer)


## FOR MORE TABLES CREATE ADDITIONAL CLASSES
## OR IDENTIFY DIFFERENT *_models.py

