from tkinter import *
from tkinter import ttk
from button import MapButton

class MapBoard(ttk.Frame):
    def __init__(self, master, rows = 3, cols = 3, **kwargs):
        super().__init__(master, **kwargs)

        self.buttons = []
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                btn = MapButton(self, text="-s-")
                
                # The Board decides where the Button goes
                btn.grid(row=r, column=c, sticky="nw") 
                
                self.buttons.append(btn)