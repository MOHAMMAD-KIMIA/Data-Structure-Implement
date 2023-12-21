# Queue class represents a simple queue data structure
class Queue:
    def __init__(self, size):
        self.size = size  # Maximum capacity of the queue
        self.queue = [None for i in range(size)]  # List to store queue elements
        self.front = self.rear = 0  # Pointers to the front and rear of the queue

    def isempty(self):
        # Check if the queue is empty
        return self.front == self.rear

    def isfull(self):
        # Check if the queue is full
        return self.rear == self.size

    def peekQueue(self):
        # Return the front element without removing it
        return self.queue[self.front]

    def enQueue(self, val):
        # Enqueue an element into the queue
        if self.isfull():
            return False  # Queue is full, cannot enqueue
        else:
            self.queue[self.rear] = val
            self.rear += 1
            return True

    def deQueue(self):
        # Dequeue an element from the queue
        if self.isempty():
            return False  # Queue is empty, cannot dequeue
        else:
            for i in range(self.rear - 1):
                self.queue[i] = self.queue[i + 1]
            self.rear -= 1

    def reverseQueue(self):
        # Reverse the elements in the queue
        start = self.front
        end = self.rear - 1
        A = self.queue
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
