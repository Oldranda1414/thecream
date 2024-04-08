"""
This module is the view
"""

import tkinter as tk

from typing import List

class View:
    """
    View class
    """
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Cream project")

        # Create a text field
        self.__texfield = tk.Text(self.__root, height=1, width=40)
        self.__texfield.pack()

        # Create a selectable list (Listbox)
        self.__listbox = tk.Listbox(self.__root, selectmode=tk.SINGLE)
        self.__listbox.pack()

        # Create a button
        self.__button = tk.Button(self.__root, text="Convert")
        self.__button.pack()

    def start(self, possible_conversions: List[str]):
        self.__add_units(possible_conversions)

        self.__root.mainloop()

    def __add_units(self, possible_conversions: List[str]):
        for item in possible_conversions:
            self.__listbox.insert(tk.END, item)
