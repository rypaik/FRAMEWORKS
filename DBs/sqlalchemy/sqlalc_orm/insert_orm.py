import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

# sqlite3 connection
# engine = create_engine('sqlite:///student_orm.db', echo=True)

# mysql connection
metadata = MetaData()

engine_link="mysql+pymysql://root:slushieCM52@localhost:3306/students_orm"
# engine_link="mysql+pymysql://root:localhost:3600/database"
engine = create_engine(engine_link, echo=True)


# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create objects  
user = Student("james","James","Boogie","MIT")
session.add(user)

user = Student("lara","Lara","Miami","UU")
session.add(user)

user = Student("eric","Eric","York","Stanford")
session.add(user)

# commit the record the database
session.commit()