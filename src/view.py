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
        self.textfield = tk.Entry(self.__root)
        self.textfield.pack()

        # Create a selectable list (Listbox)
        self.listbox = tk.Listbox(self.__root, selectmode=tk.SINGLE)
        self.listbox.pack()

        # Create a button
        self.button = tk.Button(self.__root, text="Convert")
        self.button.pack()

        self.button.bind("<Button-1>", self.__button_pressed)

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

    def __get_value(self) -> float:
        return float(self.textfield.get())

    def __button_pressed(self, _):
        unit = self.__get_unit()
        value = self.__get_value()
        pub.sendMessage("calculate_conversion", unit=unit, input=value)

    def post_result(self, value: float):
        """
        The gui will show the result to the user

        Args:
            value (float): The value to be shown
        """
        # Create a Text widget
        text_widget = tk.Text(self.__root, height=10, width=40)
        text_widget.pack()

        # Insert text into the Text widget
        msg = f"The result is equal to {value} chantilly cream"
        text_widget.insert(tk.END, msg)
