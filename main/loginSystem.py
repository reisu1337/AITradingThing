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
        return "Username already exists in database"
    else:
        if password != confPassword:
            return "Passwords do not match"
        else:
            pass

    userID = generateUserID()
    encPassword = bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt())

    writeStatement = "INSERT INTO users (id, username, password) VALUES (?,?,?)"

    cur.execute(writeStatement, (userID, username, encPassword))
    con.commit()

    return "Success"


def loginUser(username, password):

    con, cur = database.connectDataBase()

    checkUserStatement = "SELECT COUNT(*) FROM users WHERE username =?"
    loginStatement = "SELECT password FROM users WHERE username=?"
    check = (cur.execute(checkUserStatement, (username,))).fetchone()[0]

    if check >= 1:
        passwordRetrieved = (cur.execute(loginStatement, (username,))).fetchone()[0]
        print(passwordRetrieved)
    else:
        print("yoinkers")


if __name__ == "__main__":
    print(registerUser("Check It", "Honk", "Honk"))
