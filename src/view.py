"""
this module is the view
"""

class View:
    """
    this class is the main view class
    """
    def show_items(self, items):
        """

        Args:
            items (_type_): _description_
        """
        print("Todo List:")
        for index, item in enumerate(items):
            print(f"{index + 1}. {item.title} - {item.description}")
        print()

    def show_menu(self):
        print("1. Add Todo Item")
        print("2. Exit")
