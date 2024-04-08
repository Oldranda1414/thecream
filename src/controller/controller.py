"""
this module is the controller
"""

from model.model import Model
from view.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View

    def run(self):
        while True:
            self.view.show_items(self.model.get_items())
            self.view.show_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter title: ")
                description = input("Enter description: ")
                self.model.add_item(title, description)
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    controller = Controller()
    controller.run()
