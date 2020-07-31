
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def pop(self):
        if len(self.storage) >= 0:
            return self.storage.pop()
        else:
            None

    def push(self, value):
        self.storage.append(value)