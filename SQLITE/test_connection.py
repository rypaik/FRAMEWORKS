import sqlite3
from sqlite3 import Error
import argparse

parser = argparse.ArgumentParser(description='SQLite3 DB Creation Module')
parser.add_argument('db_file', type=str, help='Enter db filename with .sqlite extension as file argmument to file check')
args = parser.parse_args()

def create_connection(db_file):
    """ Checks if sqlite3 db exists, and open connection. If no dq, create sqlite3 db in current directory"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            print(f"connected to sqlite3 database: {db_file}")
            conn.close()


if __name__ == '__main__':
    create_connection(args.db_file)
