# DOCUMENTED WAY
# from sqlalchemy import create_engine
# db_url = "mysql+pymysql://root:root@localhost:13306/data"
# engine = create_engine(db_url, pool_size=5, pool_recycle=3600)

# PREFERRED WAY - Sessions Handle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('mysql+pymysql://root:root@localhost:13306/data')

session_factory = sessionmaker(bind=engine)

Session = scoped_session(session_factory)



# Thread safe Sessions Handling
import threading

from sqlalchemy.orm import sessionmaker, scoped_session

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# `threading.local()`, similar to `globals()`, but returns variables that
# are only accessible to a thread.
thread_local = threading.local()

def get_session():
    # Get a session object for each thread.
    if not hasattr(thread_local, "session"):
        thread_local.session = Session()
    return thread_local.session
