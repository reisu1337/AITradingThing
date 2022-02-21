from tkinter import *

mainui = Tk()

def main():

    mainui.title("Trading App")
    mainui.geometry("960x540")

    mainFrame = Frame(mainui)
    mainFrame.grid(row=0, column=0, sticky="nswe")

    toolbar = Frame(mainui, bg="BLUE")
    toolbar.grid(row=0, column=0, sticky="nswe")
    analysis = Frame(mainui, bg="GREEN")
    analysis.grid(row=1, column=0, sticky="nswe")
    news = Frame(mainui, bg="RED")
    news.grid(row=2, column=0, sticky="nswe")
    graph = Frame(mainui, bg="yellow")
    graph.grid(row=1, column=1, sticky="nswe")

    mainui.rowconfigure(0, weight=1)
    mainui.rowconfigure(1, weight=10)
    mainui.rowconfigure(2, weight=10)
    mainui.columnconfigure(0, weight=6)
    mainui.columnconfigure(1, weight=6)

    mainui.mainloop()


if __name__ == "__main__":
    main()