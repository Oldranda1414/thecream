"""
This module is the view
"""

from typing import Tuple
import tkinter as tk
from pubsub import pub

from utils import round_to_significant_figures

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

        # Create a button
        self.button = tk.Button(self.__root, text="Convert")
        self.button.pack()

        # Create a response Text widget
        self.response_text_widget = tk.Text(self.__root, height=10, width=40)
        self.response_text_widget.pack()

        self.button.bind("<Button-1>", self.__button_pressed)

    def start(self):
        """
        starts the gui

        Args:
            possible_conversions (List[str]): list of possible units to convert
        """
        self.__root.mainloop()

    def __get_query(self) -> Tuple[float, str]:
        textfield_contents = self.textfield.get()
        value, unit = textfield_contents.split(" ")
        return float(value), unit

    def __button_pressed(self, _):
        try:
            value, unit = self.__get_query()
        except ValueError as _:
            self.post_error("Input error. Insert a number and a unit of mesurement in this order, separated by a space")
        else:
            pub.sendMessage("calculate_conversion", unit=unit, value=value)

    def post_result(self, value: float):
        """
        The gui will show the result to the user

        Args:
            value (float): The value to be shown
        """
        if value.is_integer():
            value = int(value)
        else:
            value = round_to_significant_figures(value, 3)


        # Insert text into the Text widget
        msg = f"The result is equal to {value} chantilly cream"
        self.__post_msg(msg)

    def post_error(self, error: str):
        """
        The gui will show the error

        Args:
            error (str): the error
        """
        msg = f"The following error occured :{error}"
        self.__post_msg(msg)

    def __post_msg(self, msg: str):
        self.__clean_response_text_widget()
        self.response_text_widget.insert(tk.END, msg)

    def __clean_response_text_widget(self):
        self.response_text_widget.delete('1.0', 'end')
