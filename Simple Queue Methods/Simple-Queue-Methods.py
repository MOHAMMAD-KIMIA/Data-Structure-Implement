class Queue:
    
    def __init__(self, size):
        self.size = size 
        self.queue = [None for i in range(size)]
        self.front = self.rear = 0
        
        
    def isempty(self):
        if self.front == self.rear:
            return True
        
    def isfull(self):
        if (self.rear == self.size):
            return True
        
    def peekQueue(self):
        return self.queue[self.front]
    
    def enQueue(self, val):
        if self.isfull():
            return False

        else:
            self.queue[self.rear] = val
            self.rear = self.rear + 1

    def deQueue(self):
        if self.isempty():
            return False
        
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return temp
        
    def reverseQueue(self):
        start = self.front
        end = self.rear - 1
        A = self.queue
        while start < end: 
            A[start], A[end] = A[end], A[start] 
            start += 1
            end -= 1
