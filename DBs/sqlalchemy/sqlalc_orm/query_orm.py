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
for student in session.query(Student).order_by(Student.id):
    print(student.firstname, student.lastname)
    
# Select Single Item using filter()
for student in session.query(Student).filter(Student.firstname == 'Eric'):
    print(student.firstname, student.lastname)