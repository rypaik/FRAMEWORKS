# delete
dele = BOOKS.delete().where(BOOKS.c.genre == "non-fiction")

engine.execute(dele)
 
# write the SQL query inside the
# text() block to fetch all records
sql = text("SELECT * from BOOKS")

# Fetch all the records
result = engine.execute(sql).fetchall() 
# View the records
for record in result:
    print("\n", record)