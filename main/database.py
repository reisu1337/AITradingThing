import os.path
import sqlite3

con = None
cur = None


def connectDataBase():
    path = os.path.join(os.path.dirname(__file__), "db.sqlite3")
    # Creates a database called db.sqlite3 in the same location as the application
    conTemp = sqlite3.connect(path)
    # Establishes a connection to the database
    curTemp = conTemp.cursor()
    # Creates a cursor instance, in order to run SQL commands on the database
    return conTemp, curTemp
    # Returns these two instances to be stored in permanent variables


def createTables():
    users_sql = """
    CREATE TABLE users (
    username text PRIMARY KEY,
    password bytes NOT NULL,
    config text )
    """
    # Statement to create a table entitled users
    cur.execute(users_sql)
    # Executes this command on the database using the globally declared cursor


def verifyTables(verifycursor):
    verifycursor.execute("""SELECT sql FROM sqlite_master WHERE type='table' AND name='users'""")
    # Runs a command on the master table to check if a table called users already exists
    try:
        verifycursor.fetchone()[0]
    except TypeError:
        return False
    else:
        return True
    # If a TypeError is returned that means the table does not exist, otherwise it does and True is returned

if __name__ == "__main__":
    con, cur = connectDataBase()
    createTables()
