# Node class represents a node in a circular linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.link = None  # Reference to the next node in the linked list

# CircularLinkedList class represents a circular linked list
class CircularLinkedList:
    def __init__(self):
        self.head = None  # Reference to the head of the linked list
        self.last = None  # Reference to the last node in the circular linked list

    # Method to insert a node at the beginning of the circular linked list
    def insertAtFirst(self, data):
        # Create a new node
        newNode = Node(data)
        
        # If the circular linked list is empty, set the last and head to the new node
        if self.last is None:
            self.last = newNode
            self.last.link = self.last
            return self.last
        else:
            # Insert the new node at the beginning
            newNode.link = self.last.link
            self.last.link = newNode
            return self.last

    # Method to insert a node at the end of the circular linked list
    def insertAtEnd(self, data):
        # Create a new node
        newNode = Node(data)
        
        # If the circular linked list is empty, set the last and head to the new node
        if self.last is None:
            self.last = newNode
            self.last.link = self.last
            return self.last
        else:
            # Insert the new node at the end
            newNode.link = self.last.link
            self.last.link = newNode
            self.last = newNode
            return self.last

    # Method to insert a node after a specified value in the circular linked list
    def insertWherever(self, data, x):
        # Check if the circular linked list is empty
        if self.last is None:
            return None

        # Create a new node
        newNode = Node(data)
        
        # Initialize the current node to the first node
        thisNode = self.last.link
        
        # Traverse the circular linked list to find the specified value
        while thisNode:
            # If the specified value is found, insert the new node
            if thisNode.data == x:
                newNode.link = thisNode.link
                thisNode.link = newNode
                # Update the last node if necessary
                if thisNode == self.last:
                    self.last = newNode
                return self.last
            thisNode = thisNode.link
            # Break if the traversal completes one cycle
            if thisNode == self.last.link:
                break

    # Method to delete the first node in the circular linked list
    def deleteFirst(self):
        if self.last is None:
            return False
        elif self.last != None:
            # If there is only one node, set last to None
            if self.last.link == self.last:
                self.last = None
            else:
                # Traverse to the last node and update its link
                temp = self.last
                while temp.link != self.last:
                    temp = temp.link
                self.last = self.last.link
                temp.link = self.last 

    # Method to delete the last node in the circular linked list
    def deleteLast(self):
        if self.last is None:
            return False
        elif self.last != None:
            # If there is only one node, set last to None
            if self.last.link == self.last:
                self.last = None
            else:
                # Traverse to the second last node and update its link
                temp = self.last
                while temp.link.link != self.last:
                    temp = temp.link
                temp.link = self.last

    # Method to delete a node with a specified value in the circular linked list
    def deleteWherever(self, x):
        if self.last is None:
            return False
        
        # Check if the node to be deleted is the first node
        if self.last.link.data == x and self.last.link == self.last:
            self.last = None
        
        thisNode = self.last
        # Check if the node to be deleted is the first node
        if thisNode.data == x:
            # Traverse to the last node and update its link
            while thisNode.link != self.last:
                thisNode = thisNode.link
            thisNode.link = self.last.link
            self.last = self.last.link
            return 

        # Traverse the circular linked list to find the specified value
        while self.last.link != self.last and self.last.link.data != x:
            thisNode = thisNode.link
        
        # Check if the specified value is found
        if self.last.link.data == x:
            temp = self.last.link
            self.last = temp.link
            temp = None
        else:
            return False

    # Method to display the elements of the circular linked list
    def display(self):
        if self.last is None:
            return False

        # Start from the first node and traverse the circular linked list
        thisNode = self.last.link
        while thisNode:
            print(thisNode.data, end=" ")
            thisNode = thisNode.link
            # Break if the traversal completes one cycle
            if thisNode == self.last.link:
                break

    # Method to get the size (number of elements) of the circular linked list
    def sizeOf(self):
        size = 1
        if self.last is not None:
            # Start from the last node and traverse the circular linked list
            thisNode = self.last
            while thisNode.link is not self.last:
                thisNode = thisNode.link
                size += 1
                # Break if the traversal completes one cycle
                if thisNode == self.head:
                    break
            return size
        else:
            size = 0
            return size

    # Method to update the value of a node at a specified position
    def update(self, data, pos):
        temp = self.head
        for i in range(pos):
            temp = temp.link
        temp.data = data

    # Method to concatenate the circular linked list with another circular linked list
    def concat(self, list2):
        # Update the size of the current circular linked list
        self.size += list2.sizeOf()
        
        # Check if the second circular linked list is not empty
        if list2.head is not None:
            # Check if the first circular linked list is not empty
            if self.head is not None:
                # Concatenate the second circular linked list to the end of the first
                self.last.link = list2.head
                self.last = list2.last
                self.last.link = self.head
            else:
                # If the first circular linked list is empty, set it to the second
                self.head = list2.head
                self.last = list2.last
                self.last.link = self.head

            # Clear the second circular linked list
            list2.head = None
            list2.last = None
        
    # Method to invert the order of nodes in the circular linked list
    def invert(self):
        # Check if the circular linked list is empty or has only one node
        if self.head is None or self.head.link is None:
            return

        # Initialize variables for previous, current, and new nodes
        previous = None
        thisNode = self.head
        newNode = None

        # Traverse the circular linked list and invert the order
        while thisNode is not None:
            newNode = thisNode.link
            thisNode.link = previous
            previous = thisNode
            thisNode = newNode

        # Update the head and last of the circular linked list
        self.head = previous
        self.last.link = self.head