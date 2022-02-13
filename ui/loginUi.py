from tkinter import *
from main import loginSystem as ls

loginWindow = Tk()


def register():
    global rege1
    global rege2
    global rege3

    registerWindow = Toplevel(loginWindow)
    registerWindow.title("Register")
    registerWindow.geometry("350x230")

    regl1 = Label(registerWindow, text="Oliver's Trading Ting", font=30)
    regl2 = Label(registerWindow, text="Username:")
    rege1 = Entry(registerWindow, width=30, borderwidth=1)
    regl3 = Label(registerWindow, text="Password:")
    rege2 = Entry(registerWindow, width=30, borderwidth=1, show="*")
    regl4 = Label(registerWindow, text="Confirm Password:")
    rege3 = Entry(registerWindow, width=30, borderwidth=1, show="*")
    regb1 = Button(registerWindow, height=1, width=15, text="Register", command=registerParams)

    regl1.place(x=100, y=20)
    regl2.place(x=40, y=60)
    rege1.place(x=110, y=60)
    rege1.insert(0, "Username")
    regl3.place(x=40, y=90)
    regl4.place(x=2, y=120)
    rege2.place(x=110, y=90)
    rege2.insert(0, "Password")
    rege3.place(x=110, y=120)
    rege3.insert(0, "Password")
    regb1.place(x=110, y=160)


def login():
    global e1
    global e2

    loginWindow.geometry("350x200")
    loginWindow.title("Login")

    l1 = Label(loginWindow, text="Oliver's Trading Ting", font=(30))
    l2 = Label(loginWindow, text="Username:")
    e1 = Entry(loginWindow, width=30, borderwidth=1)
    l3 = Label(loginWindow, text="Password:")
    e2 = Entry(loginWindow, width=30, borderwidth=1, show="*")
    b1 = Button(loginWindow, height=1, width=15, text="Login", command=loginParams)
    b2 = Button(loginWindow, height=1, width=15, text="Register", command=register)

    l1.place(x=100, y=20)
    l2.place(x=40, y=60)
    e1.place(x=110, y=60)
    e1.insert(0, "Username")
    l3.place(x=40, y=90)
    e2.place(x=110, y=90)
    e2.insert(0, "Password")
    b1.place(x=50, y=130)
    b2.place(x=170, y=130)

    loginWindow.mainloop()


def loginParams():
    username = e1.get()
    password = e2.get()
    print(ls.loginUser(username, password))


def registerParams():
    username = rege1.get()
    password = rege2.get()
    confPassword = rege3.get()
    print(ls.registerUser(username, password, confPassword))


if __name__ == "__main__":
    login()
