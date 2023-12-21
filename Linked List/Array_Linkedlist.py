# Import the 'linkedList' module from 'One_Direction_Linkedlist'
from One_Direction_Linkedlist import linkedList

# Define a class 'Array' to represent an array using a linked list
class Array:
    # Initialize a linked list object as a class variable
    array = linkedList.LinkedList()
    
    # Method to add a data element at a specified position in the array
    def add(self, data, position):
        self.array.insertWherever(data, position)
    
    # Method to delete a data element at a specified position in the array
    def delete(self, position):
        return self.array.deletWherever(position)
    
    # Method to get the size (number of elements) of the array
    def size(self):
        return self.array.sizeOf()
    
    # Method to display the elements of the array
    def display(self):
        self.array.display()
