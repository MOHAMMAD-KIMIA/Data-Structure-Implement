# Import the linkedList module from the One_Direction_Linkedlist package
from One_Direction_Linkedlist import linkedList

# Stack class represents a stack using a linked list
class Stack:
    # Initialize a linked list for the stack
    stack = linkedList.LinkedList()
    
    # Method to push (add) data to the top of the stack
    def push(self, data):
        self.stack.insertAtEnd(data)
            
    # Method to pop (remove) data from the top of the stack
    def pop(self):
        return self.stack.deleteFromLast()
    
    # Method to peek at the data at the top of the stack without removing it
    def peek(self):
        return self.stack.head.data
            
    # Method to display the elements of the stack
    def display(self):
        self.stack.display()