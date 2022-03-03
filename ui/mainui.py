from tkinter import *
from main import stockHandling as sh, graphing as gr
from PIL import ImageTk, Image

mainui = Tk()
graph = None
stockRetrieved = False
img = None


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

    img = ImageTk.PhotoImage(Image.open(f"{ticker}graph.png"))
    canvas = Canvas(graph, width=640, height=480, bg="black", highlightthickness=0, relief="ridge")
    canvas.pack()
    canvas.create_image(320, 240, image=img)


if __name__ == "__main__":
    mainui.title("Trading App")
    mainui.resizable(height=False, width=False)

    toolbar = Frame(mainui, bg="BLUE")
    toolbar.grid(row=0, column=0, sticky="nswe", columnspan=2)
    analysis = Frame(mainui, bg="GREEN")
    analysis.grid(row=1, column=0, sticky="nswe")
    news = Frame(mainui, bg="RED", width=400)
    news.grid(row=2, column=0, sticky="nswe")
    graph = Frame(mainui, bg="YELLOW", width=640, height=480)
    graph.grid(row=1, column=1, sticky="nswe", rowspan=2)

    # mainui.rowconfigure(0, weight=1)
    # mainui.rowconfigure(1, weight=10)
    # mainui.rowconfigure(2, weight=10)
    # mainui.columnconfigure(0, weight=6)
    # mainui.columnconfigure(1, weight=6)

    mainui.update()
    width = graph.winfo_width()
    height = graph.winfo_height()

    print(width, height)

    loadToolbar(toolbar)
    mainui.mainloop()
