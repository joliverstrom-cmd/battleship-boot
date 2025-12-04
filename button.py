from tkinter import *
from tkinter import ttk
from functools import partial

class ModeButton(ttk.Button):
    def __init__(self, master, **kwargs):

        if "style" not in kwargs:
            kwargs["style"] = "primary.TButton"     
    
        super().__init__(master, **kwargs)

class PlacementButton(ttk.Button):
    def __init__(self, master, row, col, **kwargs):
        
        super().__init__(master, **kwargs)

        self.row = row
        self.col = col

class PlayButton(ttk.Button):
    def __init__(self, master, row, col, **kwargs):
 
        # Initialize the button with our internal check_hit method as the command
        super().__init__(master, **kwargs)
        self.row = row
        self.col = col
  
    def set_hit(self):

        self.configure(style="Hit.TButton", text=" X ")
        self.state(['disabled'])
    
    def set_miss(self):
        self.configure(style="Miss.TButton", text=" O ")
        self.state(['disabled'])
