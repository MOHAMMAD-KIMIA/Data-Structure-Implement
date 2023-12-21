# Stack class represents a simple stack data structure
class Stack:
    def __init__(self, c):
        self.stack = [None for i in range(c)]  # List to store stack elements
        self.top = -1  # Index of the top element in the stack
        self.capacity = c  # Maximum capacity of the stack

    def isempty(self):
        # Check if the stack is empty
        return self.top == -1

    def isfull(self):
        # Check if the stack is full
        return self.top == self.capacity - 1

    def push(self, x):
        # Push an element onto the stack
        if self.isfull():
            return False  # Stack is full, cannot push
        else:
            self.top += 1
            self.stack[self.top] = x
            return True

    def pop(self):
        # Pop an element from the stack
        if self.isempty():
            return False  # Stack is empty, cannot pop
        else:
            temp = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return temp

    def peek(self):
        # Return the top element without removing it
        return self.stack[self.top]