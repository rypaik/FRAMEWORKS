


# Create Database

"""
mysql> CREATE DATABASE <db_name> 

mysql> USE <db_name>
"""


# Create Table
"""
create table 'product')
    'id' inti(11) NOT NULL,
    'name' varchar(50) NOT NULL,
    'price' int(11) NOT NULL,
    'stock' int(11) NOT NULL
    );


"""


# using MySQLdb module

import MySQLdb
import csv
import sys
conn = MySQLdb.connect(host="127.0.0.1", user="root", password="", database="Fruit_Shop")

cursor = conn.cursor()
csv_data = csv.reader(open('products.csv'))
header = next(csv_data)

print('Importing the CSV Files')
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO product (id,name,price,stock) VALUES (%s, %s, %s, %s)", row)

conn.commit()
cursor.close()
print('Done')




# usign pymysql
# TEST:
import pymysql
import csv
db = pymysql.connect("localhost","root","12345678","data" )

cursor = db.cursor()
csv_data = csv.reader(open('test.csv'))
next(csv_data)
for row in csv_data:
    cursor.execute('INSERT INTO PM(col1,col2) VALUES(%s, %s)',row)

db.commit()
cursor.close()



# TEST::

import csv 
import pymysql
db = pymysql.connect( host = '###.###.##.#',
      user = 'test',passwd = 'test')
cursor = db.cursor()
f = csv.reader(open('c:/tmp/sample.csv'))
sql = """INSERT INTO test.table(test1,test2) VALUES(%s,%s)"""
next(f)
for line in f:
    line=[None if cell == '' else cell for cell in line]
    cursor.execute(sql, line)

db.commit()
cursor.close()
print ("Imported")
