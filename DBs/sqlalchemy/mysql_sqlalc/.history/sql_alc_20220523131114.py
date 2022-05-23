"""environmental"""
from dotenv import load_dotenv
import os

load_dotenv()


"""Create database connection"""
# import sqlalchemy as db
from sqlalchemy import create_engine, Table, Column, Integer, String
from sqlalchemy import MetaData

metadata_obj = MetaData()