# CS361 Group Project: Steam Game Tracker
# Trent Scoggins
# scoggint

# --CITATIONS--
# Used for learning basics of Tkinter: https://www.geeksforgeeks.org/python/python-gui-tkinter/
# Forest Theme supplied from https://github.com/rdbende/Forest-ttk-theme?tab=readme-ov-file


import csv
import os
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Get directories
root_directory = os.path.dirname(os.path.abspath(__file__))
theme_directory = os.path.join(root_directory, 'ForestThemePack')
dark_tcl = os.path.join(theme_directory, 'forest-dark.tcl')
light_tcl = os.path.join(theme_directory, 'forest-light.tcl')
data_directory = os.path.join(root_directory, "LibraryData")
library_directory = os.path.join(data_directory, "library.csv")

# Globals
cur_number_of_games = 0

def menu_add_game():

    def write_to_library():
        global cur_number_of_games
        # Get all the necessary info from the entry panels
        game_data = entry_game.get()
        developer_data = entry_developer.get()
        publisher_data = entry_publisher.get()
        date_data = entry_release_date.get()
        genre_data = entry_genre.get()

        # Concat all the data intp CSV style entry
        new_row = [game_data, developer_data, publisher_data, date_data, genre_data]

        # Write to the library.csv
        with open(library_directory, "a", newline='',) as library_file:
            # Create a CSV writer object
            writer = csv.writer(library_file)
            writer.writerow(new_row)
        
        cur_number_of_games += 1

        update_tree()
    

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
    entry_genre = Entry(add_game)
    entry_genre.grid(row=4, column=1)

    but_confirm = ttk.Button (add_game, text="Add Game", style='Accent.TButton', width=10, command=write_to_library)
    but_confirm.grid(row=5, column=0, columnspan=2)

def menu_remove_game():
    def remove_from_library():
        global cur_number_of_games
        # Remove specified game from CSV
        remove_me = int(game_id.get())

        # Use pandas instead for cleaner implimentation
        # Load the CSV
        library_CSV = pd.read_csv(library_directory)

        # Drop the specified row by its positional index
        library_CSV = library_CSV.drop(library_CSV.index[remove_me - 1])
        library_CSV.to_csv(library_directory, index=False)

        cur_number_of_games -= 1
        update_tree()


    # Remove a game by specifying its ID number
    remove_game = tk.Toplevel(main_menu)
    title_remove_game = Label(remove_game, text="Remove a game")
    title_remove_game.grid(row=0)

    # ID specification
    Label(remove_game, text="What game would you like to remove?").grid(row=1)
    Label(remove_game, text="(Please use the Entry Number)").grid(row=2)
    game_id = ttk.Spinbox(remove_game, from_=1, to=cur_number_of_games)
    game_id.grid(row=3)

    # confirm button
    but_confirm = ttk.Button(remove_game, text="Remove Game", style='Accent.TButton', width=10, command=remove_from_library)
    but_confirm.grid(row=4, pady=10)


def update_tree():
    # Purge tree and rewrite from CSV
    game_tree.delete(*game_tree.get_children())

    # Refresh the game tree
    with open(library_directory, "r", newline="") as library_file:
        reader = csv.reader(library_file)
        header = next(reader)
        for i, row in enumerate(reader):
            game_tree.insert("", "end", text=i + 1, values=row)

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
but_add_game.grid(column=1, row=1, pady=0)

# Add remove game button
but_remove_game = ttk.Button(main_menu, text= "Remove Game", width=10, command=menu_remove_game)
but_remove_game.grid(column=1, row=2, pady=0)

# Create pane for library
library_pane = ttk.PanedWindow(orient='horizontal')
library_pane.grid(row=1, column=0, pady=(10), sticky="nsew", rowspan=3)

# Create list of games using treeview
game_tree = ttk.Treeview(library_pane, selectmode='browse', columns=("col1", "col2", "col3", "col4", "col5"))
game_tree.heading("col1", text="Game Name")
game_tree.heading("col2", text="Developer")
game_tree.heading("col3", text="Publisher")
game_tree.heading("col4", text="Release Date")
game_tree.heading("col5", text="Genre")
game_tree.column("#0", width= 30)

with open(library_directory, "r", newline="") as library_file:
        reader = csv.reader(library_file)
        header = next(reader)
        for i, row in enumerate(reader):
            game_tree.insert("", "end", text=i + 1, values=row)
            cur_number_of_games += 1

game_tree.pack(side='left')

game_scroll_bar = ttk.Scrollbar(library_pane, orient='vertical', command=game_tree.yview)
game_scroll_bar.pack(side='right')
game_tree.configure(xscrollcommand = game_scroll_bar.set)

info_pane = ttk.PanedWindow(main_menu)
info_pane.grid(row=1, column=4, pady=(10), sticky="nsew", rowspan=1)


# loop
main_menu.mainloop()