from One_Direction_Linkedlist import linkedList

class Stack:
    stack = linkedList.LinkedList()
    
    def push(self, data):
        self.stack.insertAtend(data)
            
    def pop(self):
        return self.stack.deleteFromlast()
    
    def peek(self):
        return self.stack.head.data
            
    def display(self):
        self.stack.display()