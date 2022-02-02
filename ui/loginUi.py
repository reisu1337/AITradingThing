from tkinter import *
from main import loginSystem as ls

loginWindow = Tk()


def main():

    global e1
    global e2


    loginWindow.geometry("350x230")
    loginWindow.title("Login")

    l1 = Label(loginWindow, text="Oliver's Trading Ting", font=(30))
    l2 = Label(loginWindow, text="Username:")
    e1 = Entry(loginWindow, width=30, borderwidth=1)
    l3 = Label(loginWindow, text="Password:")
    e2 = Entry(loginWindow, width=30, borderwidth=1, show="*")
    b1 = Button(loginWindow, height=1, width=15, text="Login", command= loginParams)

    l1.place(x=100, y=20)
    l2.place(x=40, y=60)
    e1.place(x=110, y=60)
    e1.insert(0, "Username")
    l3.place(x=40, y=90)
    e2.place(x=110, y=90)
    e2.insert(0, "Password")
    b1.place(x = 110, y=130)

    loginWindow.mainloop()


def loginParams():
    username = e1.get()
    password = e2.get()
    ls.loginUser(username, password)


if __name__ == "__main__":
    main()

