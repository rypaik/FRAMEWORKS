


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
