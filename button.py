from tkinter import *
from tkinter import ttk
from functools import partial

class ModeButton(ttk.Button):
    def __init__(self, master, **kwargs):
        # We extract 'command' from kwargs if it exists, to prevent conflicts, 
        # though usually we want to force our own command.

        # Initialize the button with our internal check_hit method as the command
        super().__init__(master, **kwargs, style="primary.TButton")

class PlacementButton(ttk.Button):
    def __init__(self, ship_coords, master, **kwargs):
        
        super().__init__(master, **kwargs, command = lambda: self.capture_placement(ship_coords))

    def capture_placement(self, ship_coords):
        info = self.grid_info()
        row_placed = int(info["row"])
        col_placed = int(info["column"])
        tup_placed = (row_placed, col_placed)
        ship_coords.append(tup_placed)
        print(ship_coords)


class PlayButton(ttk.Button):
    def __init__(self, target_coords, master, **kwargs):
        # We extract 'command' from kwargs if it exists, to prevent conflicts, 
        # though usually we want to force our own command.
        if 'command' in kwargs:
            print("Warning: Custom command ignored in favor of check_hit")
            del kwargs['command']

        # Setting styling so buttons change color when pressed
        style = ttk.Style()

        #Style for HIT buttons (orange)
        style.map("Hit.TButton",
            foreground=[('disabled', 'orange')] 
        )
        
        # Create a style specifically for a MISS (Yellow)
        style.map("Miss.TButton",
            foreground=[('disabled', 'yellow')]
        )
 
        # Initialize the button with our internal check_hit method as the command
        super().__init__(master, command= lambda: self.check_hit(target_coords), **kwargs)
  
    def check_hit(self, target_coords):

        strike = False
        
        # Get current grid position
        info = self.grid_info()
        
        # specific check to ensure the button has actually been gridded
        if not info:
            print("Error: Button has not been placed in a grid yet.")
            return

        row_hit = int(info["row"])
        col_hit = int(info["column"])
        tup_hit = (row_hit, col_hit)
        
        if tup_hit in target_coords:
            print(f"Target hit at {row_hit}, {col_hit}!")
            strike = True
        else:
            print(f"You missed at {row_hit}, {col_hit}")

        self.update_hit_button(strike)


    def update_hit_button(self, strike):
        # Set button to pressed if it hit a target (strike = true)
        if strike:
            self.configure(style="Hit.TButton", text =" X ")
            #self.config(text=" X ")
        #If it was a miss, set to disabled
        else:
            self.configure(style="Miss.TButton", text = " O ")
            self.config(text="-O-")

        self.state(['disabled'])
        
