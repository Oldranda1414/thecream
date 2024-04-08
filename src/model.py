class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class TodoListModel:
    def __init__(self):
        self.todo_items = []

    def add_item(self, title, description):
        item = TodoItem(title, description)
        self.todo_items.append(item)

    def get_items(self):
        return self.todo_items
