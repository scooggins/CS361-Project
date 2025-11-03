# CS361 Group Project: Steam Game Tracker
# Trent Scoggins
# scoggint

# --CITATIONS--
# Used for learning basics of Tkinter: https://www.geeksforgeeks.org/python/python-gui-tkinter/
# Forest Theme supplied from https://github.com/rdbende/Forest-ttk-theme?tab=readme-ov-file

import os
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Get directories
root_directory = os.path.dirname(os.path.abspath(__file__))
theme_directory = os.path.join(root_directory, 'ForestThemePack')
dark_tcl = os.path.join(theme_directory, 'forest-dark.tcl')
light_tcl = os.path.join(theme_directory, 'forest-light.tcl')


def menu_add_game():
    # create add game menu
    add_game = tk.Toplevel(main_menu)

    title_add_game = Label(add_game, text="Add a new Steam Game")
    title_add_game.pack

    # Text entry boxes for new game
    Label(add_game, text="Game:").grid(row=0)
    entry_game = Entry(add_game)
    entry_game.grid(row=0, column=1)

    Label(add_game, text="Developer:").grid(row=1)
    entry_developer = Entry(add_game)
    entry_developer.grid(row=1, column=1)

    Label(add_game, text="Publisher:").grid(row=2)
    entry_publisher = Entry(add_game)
    entry_publisher.grid(row=2, column=1)

    Label(add_game, text="Release Date (mm/dd/yyy):").grid(row=3)
    entry_release_date = Entry(add_game)
    entry_release_date.grid(row=3, column=1)

    Label(add_game, text="Genre:").grid(row=4)
    entry_release_date = Entry(add_game)
    entry_release_date.grid(row=4, column=1)

    but_confirm = ttk.Button (add_game, text="Add Game", style='Accent.TButton', width=10, command=add_game.destroy)
    but_confirm.grid(row=5, column=0, columnspan=2)

# Create the main menu
main_menu = tk.Tk("Steam Game Tacker", "Main Menu", "Main Menu", True)

# ------Forest Theme------
main_menu.tk.call('source', dark_tcl)
ttk.Style().theme_use('forest-dark')
# ------Forest Theme------

# Add menu widgets
main_menu.title("Steam Game Tracker")

# Add new game button
but_add_game = ttk.Button(main_menu, text= "Add Game", style='Accent.TButton', width=10, command=menu_add_game)
but_add_game.grid(column=2, row=0, pady=20)

# Create pane for library
library_pane = ttk.PanedWindow(orient='horizontal')
library_pane.grid(row=1, column=0, pady=(10), sticky="nsew", rowspan=4)

# Create list of games using treeview
game_tree = ttk.Treeview(library_pane, selectmode='browse')
game_tree.pack(side='left')

game_scroll_bar = ttk.Scrollbar(library_pane, orient='vertical', command=game_tree.yview)
game_scroll_bar.pack(side='right')
game_tree.configure(xscrollcommand = game_scroll_bar.set)


info_pane = ttk.PanedWindow(main_menu)
info_pane.grid(row=1, column=4, pady=(10), sticky="nsew", rowspan=1)




# loop
main_menu.mainloop()