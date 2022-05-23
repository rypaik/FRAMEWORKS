


# SQLAlchemy Guide - Starter

[Database in Python Made Easy with SQLAlchemy](https://hackersandslackers.com/python-database-management-sqlalchemy/)





'''
[DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
'''

Database connection URI structure

- **[DB_TYPE]** -  Specifies the kind (dialect) of database we're connecting to. SQLAlchemy can interface with all mainstream flavors of relational databases. Depending on which database you're connecting to, replace [DB_TYPE] with the matching dialect:
        - MySQL: mysql
        - PostgreSQL: postgresql
        - SQLite: sqlite
        - Oracle (ugh): oracle
        - Microsoft SQL (slightly less exasperated "ugh"): mssql
- **[DB_CONNECTOR]** - To manage your database connections, SQLAlchemy leverages whichever Python database connection library you chose to use. If you aren't sure what this means, here are the libraries I'd recommend per dialect:
        - MySQL: pymysql, mysqldb
        - PostgreSQL: psycopg2, pg8000
        - SQLite: (none needed)
        - Oracle: cx_oracle
        - Microsoft SQL: pymssql, pyodbc




