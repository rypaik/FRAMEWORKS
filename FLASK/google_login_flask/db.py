import sqlite3





# DATABASE ="/tmp/flask_google.db"
conn = sqlite3.connect('flask_google.sqlite')
cursor = conn.cursor()
print("Opened database successfully")


def init_db_command():
    pass
