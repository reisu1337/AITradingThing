import os.path
import sqlite3

con = None
cur = None


def connectDataBase():
    path = os.path.join(os.path.dirname(__file__), "db.sqlite3")
    conTemp = sqlite3.connect(path)
    curTemp = conTemp.cursor()
    return conTemp, curTemp


def createTables():
    users_sql = """
    CREATE TABLE users (
    id integer PRIMARY KEY,
    username text NOT NULL,
    password text NOT NULL,
    config text NOT NULL )
    """
    cur.execute(users_sql)


def verifyTables(verifycursor):
    verifycursor.execute("""SELECT sql FROM sqlite_master WHERE type='table' AND name='usrs'""")
    try:
        verifycursor.fetchone()[0]
    except TypeError:
        return False
    else:
        return True


if __name__ == "__main__":
    con, cur = connectDataBase()
    print(verifyTables(cur))
