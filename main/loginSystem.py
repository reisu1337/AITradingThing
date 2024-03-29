from main import database
import bcrypt
from datetime import datetime


def generateUserID():
    now = datetime.now()
    currentTimeHash = bcrypt.hashpw(bytes(str(now), "utf-8"), bcrypt.gensalt())
    return str(currentTimeHash)[5:15]


def checkUsername(username):
    # Returns False if username is already in database, and True if not
    con, cur = database.connectDataBase()
    checkStatement = "SELECT COUNT(*) FROM users WHERE username =?"
    check = (cur.execute(checkStatement, (username,))).fetchone()[0]
    if check >= 1:
        return False
    else:
        return True


def registerUser(username, password, confPassword):
    con, cur = database.connectDataBase()
    if not checkUsername(username):
        return False  # "Username already exists in database"
    else:
        if password != confPassword:
            return False  # "Passwords do not match"
        else:
            pass

    encPassword = bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt())

    writeStatement = "INSERT INTO users (username, password, config) VALUES (?,?, ?)"

    cur.execute(writeStatement, (username, encPassword, ""))
    con.commit()

    return True  # "Success"


def loginUser(username, password):
    con, cur = database.connectDataBase()

    loginStatement = "SELECT password FROM users WHERE username=?"

    if not checkUsername(username):
        passwordRetrieved = (cur.execute(loginStatement, (username,))).fetchone()[0]
        if bcrypt.checkpw(bytes(password, "utf-8"), passwordRetrieved):
            return username
        else:
            return False  # "Passwords do not match"
    else:
        return False  # "Username does not match"


if __name__ == "__main__":
    print(registerUser("Oliver", "password", "password"))
