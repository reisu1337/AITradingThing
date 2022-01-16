import database


def checkUsername(username):
    # Returns False if username is already in database, and True if not
    con, cur = database.connectDataBase()
    checkStatement = "SELECT COUNT(*) FROM users WHERE username =?"
    check = (cur.execute(checkStatement, (username,))).fetchone()[0]
    if check >= 1:
        return False
    else:
        return True


def registerUser(username, password, confpassword):
    return True


if __name__ == "__main__":
    print(checkUsername("Test"))
