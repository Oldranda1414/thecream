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
    
    def calculate_conversion(self):
        print("calculating")
