from tkinter import *
from tkinter import ttk
from button import PlayButton, ModeButton, PlacementButton

class MapBoard(ttk.Frame):
    def __init__(self, master, rows = 3, cols = 3, **kwargs):
        super().__init__(master, **kwargs)
        self.rows = rows
        self.cols = cols
        
        modebtn = ModeButton(self, text="Start game", command=self.start_game)

        modebtn.grid(row=0, column = 0, columnspan=cols*4, sticky="NSEW")

        self.ship_coords = []

        self.placementbuttons = []
        
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                btn = PlacementButton(self.ship_coords, self, text="EMPTY")
                
                # The Board decides where the Button goes
                btn.grid(row=r, column=c, sticky="nw") 
                
                self.placementbuttons.append(btn)

    def start_game(self):
        self.playbuttons = []
        
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                btn = PlayButton(self.ship_coords, self, text="~s~")
                
                # The Board decides where the Button goes
                btn.grid(row=r, column=c, sticky="nw") 
                
                self.playbuttons.append(btn)