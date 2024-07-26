""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_pokemon_info


# Create the main window
root = Tk()
root.title("Pokemon Information")
root.resizable(False, False)

# TODO: Create the frames
frame_input1 = ttk.Frame(root)
frame_input1.grid(row=0, column =0, columnspan=2, pady=(20,10))

## frame for Info
frame_info = ttk.LabelFrame(root, text="Info")
frame_info.grid(row=1, column = 0, padx=(20,10), pady=(10,20), sticky=N)

##frame for Stats
frame_stats1 = ttk.LabelFrame(root, text="Stats")
frame_stats1.grid(row=1, column= 1, padx=(10,20), pady=(10,20), sticky=N)

# TODO: Populate the user input frame with widgets
lbl_name = ttk.Label (frame_input1, text="Pokemon Name:")
lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

enter_name = ttk>Entry(?????)
enter_name.????
enter_name...???


# TODO: Define button click event handler function

root.mainloop()