# Import the linkedList module from the One_Direction_Linkedlist package
from One_Direction_Linkedlist import linkedList

# Queue class represents a queue using a linked list
class Queue:
    # Initialize a linked list for the queue
    queue = linkedList.LinkedList()
    
    # Method to enqueue (add) data to the end of the queue
    def enqueue(self, data):
        self.queue.insertAtEnd(data)
            
    # Method to dequeue (remove) data from the front of the queue
    def dequeue(self):
        return self.queue.deleteFromFirst()
        
    # Method to peek at the data at the front of the queue without removing it
    def peek(self):
        return self.queue.head.data
    
    # Method to get the size (number of elements) of the queue
    def size(self):
        return self.queue.sizeOf()
            
    # Method to display the elements of the queue
    def display(self):
        self.queue.display()
