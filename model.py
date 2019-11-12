import sqlite3
import os
filename='database.db'
path=os.path.exists(filename)
if path:
    print('Already exists!')
else:
    conn=sqlite3.connect(filename)
    conn.execute('CREATE TABLE account(username TEXT, email TEXT, password TEXT)') #SQLstatement
    print('Table created successfully!')
    conn.close()
