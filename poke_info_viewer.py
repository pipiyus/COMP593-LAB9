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

enter_name = ttk.Entry(frame_input1)
enter_name.insert(0, "Diglett")
enter_name.grid(row=0, column=1)

def handle_btn_get_info():
  poke_name = enter_name.get().strip()
  if poke_name = '': return 
  poke_info = get_pokemon_info(poke_name)
  if poke_info:
    label_height_value['text'] = str(poke_info['height'] + 'dm')
    ##weight
    ##types_list
    types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
    #type_value
    #------stats
    label_type_value['text'] = ', '.join(types_list)
    bar_hp['value']= poke_info['stats'][0]['base_']

    
    

# TODO: Define button click event handler function

root.mainloop()