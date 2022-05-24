from sqlalchemy import create_engine
from sqlalchemy. ext. declarative import declarative_base
from sqlalchemy. orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# import the ‘Base’ class in the database.py file above into the models.py file below to use declarative_base()
