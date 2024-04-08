"""
This module is the view
"""

from typing import List
import tkinter as tk
from pubsub import pub

class View:
    """
    View class
    """
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Cream project")

        # Create a text field
        self.textfield = tk.Text(self.__root, height=1, width=40)
        self.textfield.pack()

        # Create a selectable list (Listbox)
        self.listbox = tk.Listbox(self.__root, selectmode=tk.SINGLE)
        self.listbox.pack()

        # Create a button
        self.button = tk.Button(self.__root, text="Convert")
        self.button.pack()

        self.button.bind("<Button-1>", lambda _: pub.sendMessage("calculate_conversion"))

    def start(self, possible_conversions: List[str]):
        """
        starts the gui

        Args:
            possible_conversions (List[str]): list of possible units to convert
        """
        self.__add_units(possible_conversions)
        self.button.bind()

        self.__root.mainloop()

    def __add_units(self, possible_conversions: List[str]):
        for item in possible_conversions:
            self.listbox.insert(tk.END, item)

    def __get_unit(self) -> str:
        # Get the index of the selected item
        index = self.listbox.curselection()[0]
        # Get the value of the selected item
        return self.listbox.get(index)
