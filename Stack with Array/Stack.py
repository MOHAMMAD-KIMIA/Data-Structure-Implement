class Stack:
    def __init__(self,c):
        self.stack = [None for i in range(c)]
        self.top = -1
        self.capacity = c

    def isempty(self):
        if self.top == 0:
            return True
        
    def isfull(self):
        if self.top == self.capacity:
            return True
        
    def push(self,x):
        if (self.isfull()):
            return False
        else:
            self.stack[self.top + 1] = x
            self.top = self.top + 1

    def pop(self):
        if(self.isempty()):
            return False
        else:
            temp = self.stack[self.top]
            self.stack[self.top] = None
            self.top = self.top - 1
            return temp

    def peek(self):
        return self.stack[self.top] 