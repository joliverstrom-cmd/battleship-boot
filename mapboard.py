from tkinter import *
from tkinter import ttk
from button import PlayButton, ModeButton, PlacementButton

class MapBoard(ttk.Frame):
    def __init__(self, master, rows = 3, cols = 3, **kwargs):
        super().__init__(master, **kwargs)
        self.rows = rows
        self.cols = cols

        style = ttk.Style()
        style.map("Hit.TButton", foreground=[('disabled', 'orange')])
        style.map("Miss.TButton", foreground=[('disabled', 'yellow')])
        
        modebtn = ModeButton(self, text="Start game", command=self.start_game)
        modebtn.grid(row=0, column = 0, columnspan=cols*4, sticky="NSEW")

        self.ships = [2,3,4]
        self.ship_coords = []
        self.placementbuttons = []
        self.placedships = []

        for ship in self.ships:
            i = 0
            while 0 < i < ship:
                (previous_x, previous_y) = self.ship_coords[-1]
                valid_x = [previous_x-1,previous_x+1]
                valid_y = [previous_y-1,previous_y+1]

        
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                btn = PlacementButton(self, r, c, text="EMPTY")
                
                btn.configure(command = lambda b=btn: self.on_place_click(b))
                btn.grid(row=r, column=c, sticky="nw") 
                
                self.placementbuttons.append(btn)

    def on_place_click(self, btn):
        
        coord = (btn.row, btn.col)
        self.ship_placer(btn, coord)

    #TODO: Create logic to cycle through multiple ships, e.g. by checking how many coordinates have been filled for each ship in self.ships
    def ship_placer(self, btn, coord ):
        if len(self.placedships) == 0:
            self.place_ship_coord(btn, coord)
            self.placedships.append(coord)
            return
        
        if self.check_valid_place(coord):
            self.place_ship_coord(btn, coord)
            self.placedships.append(coord)
            return
        else:
            print("Invalid placement, it has to be adjacent to previous placement")

            
    def place_ship_coord(self, btn, coord):
    
        print(f"Ship placed at {coord}")
        btn.configure(text="SHIP")
        self.ship_coords.append(coord)
            
    # TODO: Update valid placement logic to cater for straight line
    def check_valid_place(self, coord):
        (row, col) = coord
        (previous_row, previous_col) = self.ship_coords[-1]
        if previous_row == row+1 or previous_row == row-1:
            if previous_col == col:
                return True
        elif previous_col == col+1 or previous_col == col-1:
            if previous_row == row:
                return True
        else:
            return False   
        

    def start_game(self):
        for btn in self.placementbuttons:
            btn.destroy()
        
        self.playbuttons = []
        
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                btn = PlayButton(self, r, c, text="~s~")
                
                btn.configure(command= lambda b=btn: self.on_play_click(b))
                
                # The Board decides where the Button goes
                btn.grid(row=r, column=c, sticky="nw") 
                
                self.playbuttons.append(btn)

    def on_play_click(self, btn):
        coord = (btn.row, btn.col)

        if coord in self.ship_coords:
            print(f"Hit at {coord}")
            btn.set_hit()
        else:
            print(f"Miss at {coord}")
            btn.set_miss()