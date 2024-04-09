"""
this module is the controller
"""

from pubsub import pub

from model import Model
from view import View

class Controller:
    """
    Controller class
    """
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        pub.subscribe(self.calculate_conversion, "calculate_conversion")

    def run(self):
        """
        Starts the system
        """
        self.view.start(self.model.get_rules_dict().keys())

    def calculate_conversion(self, unit: str, value: float):
        """
        Method to calculate the conversion to chantilly cream

        Args:
            unit (str): The unit to convert from
            value (float): The value to be converted
        """
        conversion = self.model.get_conversion(unit)
        output: float = conversion(value)
        self.view.post_result(output)
