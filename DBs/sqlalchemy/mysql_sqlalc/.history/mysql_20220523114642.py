

# SQLAlchemy database engine
"""environmental"""
from dotenv import load_dotenv
import os

load_dotenv()


"""Create database connection"""
import sqlalchemy as db
from sqlalchemy import create_engine 

engine_link="mysql+pymysql://root:slushieCM52@localhost:3600/testdb"
# engine_link="mysql+pymysql://root:localhost:3600/database"
engine = create_engine(engine_link, echo=True)

connection = engine.connect()







