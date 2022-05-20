from sqlalchemy_utils import create_database, database_exists

db_url = "mysql+pymysql://root:root@localhost:13306/data"

if not database_exists(db_url):
    create_database(db_url)
