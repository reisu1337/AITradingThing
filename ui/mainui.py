from tkinter import *
from main import stockHandling as sh, graphing as gr, newsSystem as ns, loginSystem as ls, analysisSystem as anas, \
    favouriteSystem as fs
from PIL import ImageTk, Image
import os
from datetime import datetime
import webbrowser

today = datetime.today()
d4 = today.strftime("%b-%d-%Y")
path = os.fsencode(os.path.dirname(__file__))

mainui = Tk()
graph = None
stockRetrieved = False
currentStock = ""
img = None
favs = ""
userLoggedIn = None


def clearImgCache():
    for file in os.listdir(path):
        filename = os.fsencode(file)
        if filename.endswith(bytes(".png", "utf-8")):
            if not filename.startswith(bytes(d4, "utf-8")):
                os.remove(path + bytes("\\", "utf-8") + file)


def tickerUI(p1="Enter Ticker"):
    tickerUIWindow = Toplevel(mainui)
    tickerUIWindow.title("Enter Ticker")

    insertData = p1

    entry1 = Entry(tickerUIWindow, width=50, borderwidth=2)
    entry1.grid(row=0, column=0)
    entry1.insert(0, insertData)

    def onClick():

        global currentStock

        ticker = entry1.get()
        if not 1 <= len(ticker) <= 5:
            label = Label(tickerUIWindow, text="Invalid Ticker")
            label.grid(row=2, column=0)
        elif not sh.retrieveData(ticker):
            label = Label(tickerUIWindow, text="Stock Not Found")
            label.grid(row=2, column=0)
        else:
            currentStock = ticker
            tickerUIWindow.destroy()
            gr.main(ticker)
            showGraph(ticker)
            showAnalysis(ticker)
            showNews(ticker)
            mainui.title(f"Trading App - {ticker.upper()}")

    button = Button(tickerUIWindow, text="Continue", command=onClick)
    button.grid(row=1, column=0)


def loadToolbar(toolbarelement):
    addstock = Button(toolbarelement, text="Add Ticker", command=tickerUI)
    loginButton = Button(toolbarelement, text="Login", command=login)
    favouriteList = Button(toolbarelement, text="Favorite List", command=favouriteListUI)
    favouriteAdd = Button(toolbarelement, text="Add to Favourites", command=addToFav)
    logOut = Button(toolbarelement, text="Sign Out", command=onSignOut)
    newsButton = Button(toolbarelement, text="More News", command=moreNewsButton)
    loginButton.grid(column=0, row=0)
    addstock.grid(column=1, row=0)
    favouriteList.grid(column=2, row=0)
    favouriteAdd.grid(column=3, row=0)
    newsButton.grid(column=4, row=0)
    logOut.grid(column=5, row=0)


def moreNewsButton():
    link = ns.getMoreNewsLink(currentStock)
    webbrowser.open(link, new=2)


def showGraph(ticker):
    global img

    for widget in graph.winfo_children():
        widget.destroy()

    img = ImageTk.PhotoImage(Image.open(f"{d4 + ticker}graph.png"))
    canvas = Canvas(graph, width=640, height=480, bg="black", highlightthickness=0, relief="ridge")
    canvas.pack()
    canvas.create_image(320, 240, image=img)


def showAnalysis(ticker):
    for widget in analysis.winfo_children():
        widget.destroy()

    heading = Label(analysis, text="Analysis", anchor="n", font="15")
    heading.grid(column=0, row=0)

    x, y = anas.regLine(ticker)
    start, end = sh.getAnalysisPrices()

    currentPrice = f"Current Price - {end}"
    projectedPrice = f"Projected Price - {round(y[-1][0], 2)}"
    priceDifference = f"Price Difference - {round(end - start, 2)}"
    projectedPriceDifference = f"Projected Price Difference - {round((y[-1][0] - y[0][0]), 2)}"

    if round((y[-1][0] - y[0][0]), 2) > 0:
        text = "This stock has a positive, upward trend. "
    else:
        text = "This stock has a negative, downward trend. "

    if end < round(y[-1][0], 2):
        text += "Using the data from the past year, we projected that this stock would end up more expensive than it " \
                "has. "
    else:
        text += "Using the data from the past year, we projected that this stock would end up less expensive than it " \
                "has. "

    cp = Message(analysis, width=400, text=currentPrice, anchor="center")
    cp.grid(column=0, row=1)

    pp = Message(analysis, width=400, text=projectedPrice, anchor="center")
    pp.grid(column=0, row=2)

    pd = Message(analysis, width=400, text=priceDifference, anchor="center")
    pd.grid(column=0, row=3)

    ppd = Message(analysis, width=400, text=projectedPriceDifference, anchor="center")
    ppd.grid(column=0, row=4)

    antext = Message(analysis, width=400, text=text, anchor="center")
    antext.grid(column=0, row=5)


def showNews(ticker):
    for widget in news.winfo_children():
        widget.destroy()

    heading = Label(news, text="News", anchor="n", font="15")
    h1, h2, h3, l1, l2, l3 = ns.getNews(ticker)

    heading.grid(column=0, row=0)

    link1 = Message(news, width=400, text=h1, fg="blue", cursor="hand2", anchor="center")
    link1.grid(column=0, row=1)
    link1.bind("<Button-1>", lambda e: webbrowser.open(l1, new=2))

    link2 = Message(news, width=400, text=h2, fg="blue", cursor="hand2", anchor="center")
    link2.grid(column=0, row=2)
    link2.bind("<Button-1>", lambda e: webbrowser.open(l2, new=2))

    link3 = Message(news, width=400, text=h3, fg="blue", cursor="hand2", anchor="center")
    link3.grid(column=0, row=3)
    link3.bind("<Button-1>", lambda e: webbrowser.open(l3, new=2))


def register():
    global rege1
    global rege2
    global rege3
    global registerWindow

    registerWindow = Toplevel(loginWindow)
    registerWindow.title("Register")
    registerWindow.geometry("350x230")

    regl1 = Label(registerWindow, text="Oliver's Trading Thing", font=30)
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
    global loginWindow

    loginWindow = Toplevel(mainui)
    loginWindow.geometry("350x200")
    loginWindow.title("Login")

    l1 = Label(loginWindow, text="Oliver's Trading Thing", font=30)
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
    global favs, userLoggedIn

    username = e1.get()
    password = e2.get()
    result = ls.loginUser(username, password)
    if isinstance(result, str):
        loginWindow.destroy()
        userLoggedIn = result
        favs = fs.getFavString(username).rstrip(",")


def registerParams():
    username = rege1.get()
    password = rege2.get()
    confPassword = rege3.get()
    if ls.registerUser(username, password, confPassword):
        registerWindow.destroy()


def onSignOut():
    global favs, userLoggedIn

    fs.setFavString(userLoggedIn, favs)
    userLoggedIn = None


def favouriteListUI():
    global favs, favsUIWindow

    if userLoggedIn is None:
        return False

    favsUIWindow = Toplevel(mainui)
    favsUIWindow.title("Favourites")

    favsList = favs.split(",")
    print(favsList)
    for i in favsList:
        if i:
            Button(favsUIWindow, text=i, command=lambda m=i: favButtonOnClick(m)).pack()
        else:
            pass


def addToFav():
    global favs, currentStock
    print(favs)
    favs = "," + currentStock + favs
    print(favs)


def favButtonOnClick(m):
    favsUIWindow.destroy()
    ticker = m
    tickerUI(ticker)


if __name__ == "__main__":
    clearImgCache()

    mainui.title("Trading App")
    mainui.resizable(height=False, width=False)

    toolbar = Frame(mainui, height=28, highlightbackground="black", highlightthickness=1)
    toolbar.grid(row=0, column=0, sticky="nswe", columnspan=2)
    analysis = Frame(mainui, height=240, width=400, highlightbackground="black", highlightthickness=1)
    analysis.grid(row=1, column=0, sticky="nswe")
    news = Frame(mainui, height=240, width=400, highlightbackground="black", highlightthickness=1)
    news.grid(row=2, column=0, sticky="nswe")
    graph = Frame(mainui, width=640, height=480, highlightbackground="black", highlightthickness=1)
    graph.grid(row=1, column=1, sticky="nswe", rowspan=2)

    loadToolbar(toolbar)

    mainui.update()
    width = toolbar.winfo_width()
    height = toolbar.winfo_height()

    mainui.mainloop()
