from main import database


def getFavString(username):

    con, cur = database.connectDataBase()
    loginStatement = "SELECT config FROM users WHERE username=?"
    favString = cur.execute(loginStatement, (username,)).fetchone()[0]
    return favString


def setFavString(username, favStringToWrite):
    con, cur = database.connectDataBase()

    writeStatement = "UPDATE users SET config=? WHERE username=?"
    cur.execute(writeStatement, (favStringToWrite, username,))
    con.commit()
