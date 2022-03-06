from tkinter import *
from main import stockHandling as sh, graphing as gr, stockClass as sc
from PIL import ImageTk, Image
import os
from datetime import datetime

today = datetime.today()
d4 = today.strftime("%b-%d-%Y")
path = os.fsencode(os.path.dirname(__file__))

mainui = Tk()
graph = None
stockRetrieved = False
img = None


def clearImgCache():
    for file in os.listdir(path):
        filename = os.fsencode(file)
        if filename.endswith(bytes(".png", "utf-8")):
            if not filename.startswith(bytes(d4, "utf-8")):
                os.remove(path + bytes("\\", "utf-8") + file)


def tickerUI():
    tickerUIWindow = Toplevel(mainui)
    tickerUIWindow.title("Enter Ticker")

    e1 = Entry(tickerUIWindow, width=50, borderwidth=2)
    e1.grid(row=0, column=0)
    e1.insert(0, "Enter your name")

    def onClick():
        ticker = e1.get()
        if not sh.retrieveData(ticker):
            label = Label(tickerUIWindow, text="Stock not found")
            label.grid(row=2, column=0)
        else:
            tickerUIWindow.destroy()
            gr.main(ticker)
            showGraph(ticker)
            mainui.title(f"Trading App - {ticker.upper()}")

    button = Button(tickerUIWindow, text="Continue", command=onClick)
    button.grid(row=1, column=0)


def loadToolbar(toolbarelement):
    addstock = Button(toolbarelement, text="Add Ticker", command=tickerUI)
    addstock.grid(column=0, row=0)


def showGraph(ticker):
    global img

    for widget in graph.winfo_children():
        widget.destroy()

    img = ImageTk.PhotoImage(Image.open(f"{d4+ticker}graph.png"))
    canvas = Canvas(graph, width=640, height=480, bg="black", highlightthickness=0, relief="ridge")
    canvas.pack()
    canvas.create_image(320, 240, image=img)


if __name__ == "__main__":

    clearImgCache()

    mainui.title("Trading App")
    mainui.resizable(height=False, width=False)

    toolbar = Frame(mainui, highlightbackground="black", highlightthickness=1)
    toolbar.grid(row=0, column=0, sticky="nswe", columnspan=2)
    analysis = Frame(mainui, highlightbackground="black", highlightthickness=1)
    analysis.grid(row=1, column=0, sticky="nswe")
    news = Frame(mainui, width=400, highlightbackground="black", highlightthickness=1)
    news.grid(row=2, column=0, sticky="nswe")
    graph = Frame(mainui, width=640, height=480, highlightbackground="black", highlightthickness=1)
    graph.grid(row=1, column=1, sticky="nswe", rowspan=2)

    mainui.update()
    width = graph.winfo_width()
    height = graph.winfo_height()

    print(width, height)

    loadToolbar(toolbar)
    mainui.mainloop()
