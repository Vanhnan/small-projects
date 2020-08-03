import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_rows(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM music")

    rows = cur.fetchall()
##    for i in rows:
##        res+=str(i)

    return rows

##c = create_connection("db_0.db")
##print(select_all_rows(c))
