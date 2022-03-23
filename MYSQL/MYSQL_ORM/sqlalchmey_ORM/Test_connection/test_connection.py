import logging

from codetiming import Timer
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)
timer = Timer("example", text="Time spent: {:.6f}", logger=logging.info)

db_url = "mysql+pymysql://root:root@localhost:13306/data"
engine = create_engine(db_url, pool_size=5, pool_recycle=3600)

with timer:
    # A new connection is created with some overhead.
    conn = engine.connect()
# INFO:root:Time spent: 0.004648

# The connection is recycled back to the pool after it's closed for efficient reuse.
conn.close()

with timer:
    # The connection is fetched from the pool directly, thus much faster.
    conn = engine.connect()
# INFO:root:Time spent: 0.000033
