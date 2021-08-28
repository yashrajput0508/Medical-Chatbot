import sqlite3 as sql
import datetime


def database():
    conn = sql.connect("database.db")
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM datas")
        conn.commit()
        c.close()
    except sql.OperationalError:
        c.execute("CREATE TABLE datas(id INTEGER PRIMARY KEY AUTOINCREMENT,username varchar(255),emailid varchar(255),contactno varchar(255),password varchar(255))")
        conn.commit()
        c.close()

def updatedatabase(username,email,contact,password):
    conn=sql.connect("database.db")
    c=conn.cursor()
    c.execute("INSERT INTO datas(username,emailid,contactno,password) VALUES(?,?,?,?);",(username,email,contact,password,))
    conn.commit()
    c.close()

def getlist(username):
    conn=sql.connect('database.db')
    c=conn.cursor()
    try:
        c.execute("SELECT password from datas WHERE username=(?);",(username,))
        l=c.fetchall()
        c.close()
        return l
    except Exception:
        c.close()
        return None

def getnumber(username,password):
    conn = sql.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT contactno from datas WHERE username=(?) AND password=(?);", (username,password))
    l = c.fetchall()
    c.close()
    return l

