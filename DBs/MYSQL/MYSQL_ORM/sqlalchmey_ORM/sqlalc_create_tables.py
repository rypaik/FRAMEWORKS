
from sqlalchemy import create_engine

from product_stocks import metadata

db_url = "mysql+pymysql://root:root@localhost:13306/data"

engine = create_engine(db_url, pool_size=5, pool_recycle=3600)

metadata.create_all(bind=engine)
