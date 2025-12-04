from tkinter import *
from tkinter import ttk
from mapboard import MapBoard


def main():

    root = Tk()



    board = MapBoard(root,4,4)

    board.grid(column=4, row=4, sticky=(N, W, E, S))

    root.mainloop()


if __name__ == "__main__":
    main()
