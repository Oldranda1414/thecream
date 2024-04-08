"""
This module is the entry point of the system
"""

from controller.controller import Controller
from model.model import Model
from view.view import View

if __name__ == "__main__":
    controller = Controller(Model(), View())
    controller.run()
