from tkinter import *
from tkinter import ttk

class MapButton(ttk.Button):
    def __init__(self, master, **kwargs):
        # We extract 'command' from kwargs if it exists, to prevent conflicts, 
        # though usually we want to force our own command.
        if 'command' in kwargs:
            print("Warning: Custom command ignored in favor of check_hit")
            del kwargs['command']
            
        # Initialize the button with our internal check_hit method as the command
        super().__init__(master, command=self.check_hit, **kwargs)
    
    def check_hit(self):
        # Define the target
        target = (1, 2)
        
        # Get current grid position
        info = self.grid_info()
        
        # specific check to ensure the button has actually been gridded
        if not info:
            print("Error: Button has not been placed in a grid yet.")
            return

        row_hit = int(info["row"])
        col_hit = int(info["column"])
        tup_hit = (row_hit, col_hit)

        if tup_hit == target:
            print(f"Target hit at {row_hit}, {col_hit}!")
        else:
            print(f"You missed at {row_hit}, {col_hit}")


