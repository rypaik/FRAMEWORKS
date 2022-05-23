"""environmental"""
from dotenv import load_dotenv
import os

load_dotenv()


"""Create database connection"""
# import sqlalchemy as db
from sqlalchemy import create_engine, Table, Column, Integer, String
from sqlalchemy import MetaData

metadata_obj = MetaData()

engine_link="mysql+pymysql://root:slushieCM52@localhost:3306/testdb"
# engine_link="mysql+pymysql://root:localhost:3600/database"
engine = create_engine(engine_link, echo=True)

# connection = engine.connect()




students = Table('student', metadata_obj,
    Column('id', Integer, primary_key = True), 
    Column('name', String(20)), 
    Column('lastname', String(20)), 
)


metadata_obj.create_all(engine)
