

# SQLAlchemy database engine
"""environmental"""
from dotenv import load_dotenv
import os

load_dotenv()


"""Create database connection"""
from sqlalchemy import create_engine

engine_link="mysql+pymysql://user:password@localhost:3600/database"
engine = create_engine(engine_link, echo=True)

connection = engine.connect()







