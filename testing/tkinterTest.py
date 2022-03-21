from tkinter import *

root = Tk()


def main():
    e = Entry(root, width=50, borderwidth=5)
    e.grid(row=0, column=0)
    e.insert(0, "googl")

    def myClick():
        label = Label(root, text=e.get())
        label.grid(row=2, column =0)

    button = Button(root, text="Click the button!", command=myClick)
    button.grid(row = 1, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()
