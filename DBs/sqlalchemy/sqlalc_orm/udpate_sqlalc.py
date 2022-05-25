"""

from sqlalchemy import update
upd = update(tablename)
val = upd.values({"column_name":"value"})
cond = val.where(tablename.c.column_name == value)

"""

from sqlalchemy import text
 
# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']
 
# update
u = update(BOOKS)
u = u.values({"genre": "sci-fi"})
u = u.where(BOOKS.c.genre == "fiction")
engine.execute(u)
 
# write the SQL query inside the text()
# block to fetch all records
sql = text("SELECT * from BOOKS")
 
# Fetch all the records
result = engine.execute(sql).fetchall()
 
# View the records
for record in result:
    print("\n", record)
