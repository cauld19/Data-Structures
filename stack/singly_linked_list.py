class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        
    def add_to_tail(self,value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1
        
    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value
        
    def remove_tail(self):
        if self.head is None:
            return None
        elif self.head.next_node is None:
            cur = self.head.get_value()
            self.head = None
            self.length -= 1
            return cur
        else:
            prev = None
            cur = self.head
            while cur.next_node is not None:
                prev = cur
                cur = cur.next_node
            prev.next_node = None
            self.length -= 1
            return cur.value

        
            
    
    def contains(self, value):
        if self.head is None:
            return None
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return True
                current = current.next_node
            return False
                    
    
    def get_max(self):
        if self.head is None:
            return None
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
                cur_node = cur_node.get_next()
        return cur_max