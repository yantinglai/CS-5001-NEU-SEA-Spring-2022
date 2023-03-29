
class Stack:
    """A stack class"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
