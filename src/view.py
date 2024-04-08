class TodoListView:
    def show_items(self, items):
        print("Todo List:")
        for index, item in enumerate(items):
            print(f"{index + 1}. {item.title} - {item.description}")
        print()

    def show_menu(self):
        print("1. Add Todo Item")
        print("2. Exit")
