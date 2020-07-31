class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        return self.storage.insert(0,value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop()
        else:
            None