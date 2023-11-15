class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)] 
        self.front = self.rear = -1

    def isempty(self):
        if self.front == -1:
            return True
        
    def isfull(self):
        if ((self.front == 0 and self.rear == -1) or ((self.rear+1) % self.size == self.front )):
            return True

    def peekQueue(self):
        return self.queue[self.front]

    def enQueue(self, val):
        if self.isfull():
            return False
        
        elif self.isempty():
            self.front = self.rear = 0
            self.queue[self.rear] = val

        else:
            self.rear = (self.rear + 1) % self.size 
            self.queue[self.rear] = val

    
    def deQueue(self):
        if self.isempty():
            return False
                    
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return temp
   
    def reverseList(self): 
        start = self.front
        end = self.rear
        A = self.queue
        while start < end: 
            A[start], A[end] = A[end], A[start] 
            start += 1
            end -= 1