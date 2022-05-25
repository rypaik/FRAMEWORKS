from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# sqlite3 method
engine = create_engine('sqlite:///student_orm.db', echo=True)

# mysql method
metadata = MetaData()

# engine_link="mysql+pymysql://root:slushieCM52@localhost:3306/students_orm"
# engine_link="mysql+pymysql://root:localhost:3600/database"
# engine = create_engine(engine_link, echo=True)

 
 
 
# declarative Method
Base = declarative_base()

class Student(Base):
    """"""
    __tablename__ = "student"
 
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    firstname = Column(String(20))
    lastname = Column(String(20))
    university = Column(String(20))

    #----------------------------------------------------------------------
    def __init__(self, username, firstname, lastname, university):
        """"""
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.university = university
        

# Create tables
Base.metadata.create_all(engine)