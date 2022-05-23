

# SQLAlchemy database engine
"""environmental"""
from dotenv import load_dotenv
import os

load_dotenv()


"""Create database connection"""
# import sqlalchemy as db
from sqlalchemy import create_engine, Table, Column, Integer, String, Metadata 

engine_link="mysql+pymysql://root:slushieCM52@localhost:3306/testdb"
# engine_link="mysql+pymysql://root:localhost:3600/database"
engine = create_engine(engine_link, echo=True)

connection = engine.connect()



""" Create Table Using SQLAlchemy"""
meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key = True), 
    Column('name', String), 
    Column('lastname', String), 
)

meta.create_all(engine)
# metadata = db.MetaData()
# metadata = db.MetaData()
# print(metadata)
# testdb = db.Table('testdb', metadata, autoload=True, autoload_with=engine)
# print(testdb.clumns.keys())







