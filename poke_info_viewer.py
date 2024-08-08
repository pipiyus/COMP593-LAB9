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

# Create the frames
frm_input = ttk.Frame(root)
frm_input.grid(row=0, column=0, columnspan=2, pady=(20,10))

## frame for Info
frm_info = ttk.LabelFrame(root, text="Info")
frm_info.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

## Frame for stats
frm_stats = ttk.LabelFrame(root, text="Stats")
frm_stats.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky=N)

# Populate the user input frame with widgets
lbl_name = ttk.Label(frm_input, text="Pokemon Name:")
lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

enter_name = ttk.Entry(frm_input)
enter_name.insert(0, "Diglett")
enter_name.grid(row=0, column=1)

def handle_btn_get_info():
    poke_name = enter_name.get().strip()
    if poke_name == '': return
    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        lbl_height_val['text'] = str(poke_info['height']) + ' dm'
        lbl_weight_val['text'] = str(poke_info['weight']) + ' hg'
        types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
       
        # Display types
        lbl_type_val['text'] = ', '.join(types_list)

        # Update stats
        bar_hp['value'] = poke_info['stats'][0]['base_stat']
        bar_attack['value'] = poke_info['stats'][1]['base_stat']
        bar_defense['value'] = poke_info['stats'][2]['base_stat']
        bar_special_attack['value'] = poke_info['stats'][3]['base_stat']
        bar_special_defense['value'] = poke_info['stats'][4]['base_stat']
        bar_speed['value'] = poke_info['stats'][5]['base_stat']
    else:
        error_message = f"Pokémon '{poke_name}' not found. Please enter a valid Pokémon name."
        messagebox.showerror(title='Error', message=error_message)

btn_get_info = ttk.Button(frm_input, text="Get Info", command=handle_btn_get_info)
btn_get_info.grid(row=0, column=2, padx=(10,0), pady=10)

# Populate the Info frame with widgets
lbl_height = ttk.Label(frm_info, text="Height:")
lbl_height.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)
lbl_height_val = ttk.Label(frm_info, width=20)
lbl_height_val.grid(row=0, column=1, padx=(0,10), pady=(10,5))

lbl_weight = ttk.Label(frm_info, text="Weight:")
lbl_weight.grid(row=1, column=0, padx=(10,5), pady=(10,5), sticky=E)
lbl_weight_val = ttk.Label(frm_info, width=20)
lbl_weight_val.grid(row=1, column=1, padx=(0,10), pady=(10,5))

lbl_type = ttk.Label(frm_info, text="Type(s):")
lbl_type.grid(row=2, column=0, padx=(10,5), pady=(10,5), sticky=E)
lbl_type_val = ttk.Label(frm_info, width=20)
lbl_type_val.grid(row=2, column=1, padx=(0,10), pady=(10,5))

# Populate the Stats frame with widgets
STAT_MAX_VALUE = 255.0
PRG_BAR_LENGTH = 200

lbl_hp = ttk.Label(frm_stats, text="HP:")
lbl_hp.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)
bar_hp = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_hp.grid(row=0, column=1, padx=(0,10), pady=(10,5))

lbl_attack = ttk.Label(frm_stats, text="Attack:")
lbl_attack.grid(row=1, column=0, padx=(10,5), pady=(5,5), sticky=E)
bar_attack = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_attack.grid(row=1, column=1, padx=(0,10), pady=(5,5))

lbl_defense = ttk.Label(frm_stats, text="Defense:")
lbl_defense.grid(row=2, column=0, padx=(10,5), pady=(5,5), sticky=E)
bar_defense = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_defense.grid(row=2, column=1, padx=(0,10), pady=(5,5))

lbl_special_attack = ttk.Label(frm_stats, text="Special Attack:")
lbl_special_attack.grid(row=3, column=0, padx=(10,5), pady=(5,5), sticky=E)
bar_special_attack = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_special_attack.grid(row=3, column=1, padx=(0,10), pady=(5,5))

lbl_special_defense = ttk.Label(frm_stats, text="Special Defense:")
lbl_special_defense.grid(row=4, column=0, padx=(10,5), pady=(5,5), sticky=E)
bar_special_defense = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_special_defense.grid(row=4, column=1, padx=(0,10), pady=(5,5))

lbl_speed = ttk.Label(frm_stats, text="Speed:")
lbl_speed.grid(row=5, column=0, padx=(10,5), pady=(5,10), sticky=E)
bar_speed = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGTH, maximum=STAT_MAX_VALUE)
bar_speed.grid(row=5, column=1, padx=(0,10), pady=(5,10))

root.mainloop()
