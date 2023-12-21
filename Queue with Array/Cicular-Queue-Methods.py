# CircularQueue class represents a circular queue data structure
class CircularQueue:

    def __init__(self, size):
        self.size = size  # Maximum capacity of the circular queue
        self.queue = [None for i in range(size)]  # List to store circular queue elements
        self.front = self.rear = -1  # Pointers to the front and rear of the circular queue

    def isempty(self):
        # Check if the circular queue is empty
        return self.front == -1

    def isfull(self):
        # Check if the circular queue is full
        return (self.front == 0 and self.rear == -1) or ((self.rear + 1) % self.size == self.front)

    def peekQueue(self):
        # Return the front element without removing it
        return self.queue[self.front]

    def enQueue(self, val):
        # Enqueue an element into the circular queue
        if self.isfull():
            return False  # Circular queue is full, cannot enqueue
        elif self.isempty():
            self.front = self.rear = 0
            self.queue[self.rear] = val
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = val

    def deQueue(self):
        # Dequeue an element from the circular queue
        if self.isempty():
            print("The circular queue is empty!")
            return
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return temp

    def reverseQueue(self):
        # Reverse the elements in the circular queue
        start = self.front
        end = self.rear
        A = self.queue
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1