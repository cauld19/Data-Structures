"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from stack import Stack
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def fn(self, array):
        for value in array:
            return value

    # Insert the given value into the tree
    def insert(self, value):
        cur_node = self
        while cur_node:
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = BSTNode(value)
                    return value
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = BSTNode(value)
                    return value
                else:
                    cur_node = cur_node.right
            


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        cur_node = self
        if self is None:
            return False
        elif cur_node.value is target:
            return True
        else:
            while cur_node:
                if target < cur_node.value:
                    if cur_node.left is None:
                        return False
                    elif target is not cur_node.left.value:
                        cur_node = cur_node.left
                    else:
                        return True
                else:
                    if cur_node.right is None:
                        return False
                    elif target is not cur_node.right.value:
                        cur_node = cur_node.right
                    else:
                        return True
                    
        
        
    # Return the maximum value found in the tree
    def get_max(self):
        cur_node = self
                
        # nothing
        if self is None:
            return None
        
        # max right
        cur_max = self.value
        while cur_node:
            if cur_node.right is None:
                return cur_max
            elif cur_node.right.value > cur_max:
                cur_max = cur_node.right.value
                cur_node = cur_node.right
            elif cur_node.right.value < cur_max:
                cur_node = cur_node.right.left
            else:
                return cur_max
                
        

                
    
                
            
        
        
    
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self:
            if self.left:
                self.left.in_order_print()
            print(self.value)
            if self.right:
                self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        if self is None:
            return None
        queue = []
        queue.append(self)
        
        while len(queue) > 0:
            print(queue[0].value)
            node = queue.pop(0)
            
            if node.left: 
                queue.append(node.left) 
  
            if node.right: 
                queue.append(node.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    
    ## in order
    
    # def dft_print(self):
    #     node = self
        
    #     stack = []
    #     while True:
    #         if node is not None:
    #             stack.append(node)
    #             node = node.left
    #         elif(stack):
    #             node = stack.pop()
    #             print(node.value)
    #             node = node.right
    #         else:
    #             break
            
    # ## preorder
    
    # def dft_print(self):
    #     node = self
        
    #     stack = []
    #     stack.append(node)
    #     while len(stack) > 0:
    #         node = stack.pop()
    #         print(node.value)
            
    #         if node.right:
    #             stack.append(node.right)
                
    #         if node.left:
    #             stack.append(node.left)
                
    ## postorder
    
    def dft_print(self):
        node = self
        
        stack = []
        stack.append(node)
        stack2 = []
        
        while stack:
            node = stack.pop()
            stack2.append(node.value)
            
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
                
        while stack2:
            print(stack2.pop())
                
            
    
            

                
               
            
        
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass
    
herm = BSTNode(10)

herm.insert(5)
herm.insert(7)
herm.insert(6)
herm.insert(3)
herm.insert(4)
herm.insert(2)

herm.dft_print()

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_dft()  
