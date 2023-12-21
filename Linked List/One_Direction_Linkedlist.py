# Node class represents a node in a linked list
class Node:
    def __init__(self, data):
        # Initialize a new Node with the given data and a null link
        self.data = data
        self.link = None

# LinkedList class represents a singly linked list
class LinkedList:
        
    def __init__(self):
        # Initialize a new linked list with a null head and last
        self.head = None
        self.last = None
        
    # Method to insert a node at the beginning of the linked list
    def insertAtFirst(self, data):
        # Insert a new node at the beginning with the given data
        newNode = Node(data)
        
        # If the linked list is empty, set the head to the new node
        if self.head is None:
            self.head = newNode
        # If the linked list is not empty, set the new node's link to the current head and update the head
        else:
            newNode.link = self.head
            self.head = newNode
            
    # Method to insert a node at the end of the linked list
    def insertAtEnd(self, data):
        # Insert a new node at the end with the given data
        newNode = Node(data)
        
        # If the linked list is empty, set both head and last to the new node
        if self.head is None:
            self.head = newNode
            self.last = newNode
        # If the linked list is not empty, append the new node to the end and update last
        else:
            self.last.link = newNode
            self.last = newNode

    # Method to insert a node at a specific position in the linked list
    def insertWherever(self, data, pos):
        # Insert a new node with the given data at a specific position in the linked list
        newNode = Node(data)
        position = 1
        thisNode = self.head
        
        # Handle the case where the linked list is empty
        if position == pos:
            self.insertAtFirst(newNode)
        # Handle the case where the linked list is not empty
        else:
            # Search for the index in the linked list
            while thisNode is not None and position + 1 is not pos:
                position += 1
                thisNode = thisNode.link
            # When the position is found, insert the new node at that position
            if thisNode is not None:
                newNode.link = thisNode.link
                thisNode.link = newNode
            # When the position is not found, return False
            else:
                return False

    # Method to delete the first node in the linked list
    def deleteFromFirst(self):
        # Delete the first node in the linked list
        if self.head is not None:
            self.head = self.head.link

    # Method to delete the last node in the linked list
    def deleteFromLast(self):
        # Delete the last node in the linked list
        if self.head is not None:
            thisNode = self.head
            # Traverse the linked list to find the second last node and set its link to None
            while thisNode.link.link is not None:
                thisNode = thisNode.link
            thisNode.link = None

    # Method to delete a node at a specific position in the linked list
    def deleteWherever(self, pos):
        # Delete the node at the specified position in the linked list
        position = 1
        thisNode = self.head
        
        # Handle the case where the linked list is not empty
        if self.head is not None:
            # If the position to delete is the first node, call deleteFromFirst()
            if position == pos:
                self.deleteFromFirst()
            else:
                # Traverse the linked list to find the node at the specified position and delete it
                while thisNode is not None and position + 1 is not pos:
                    position += 1
                    thisNode = thisNode.link
                if thisNode is not None:
                    thisNode.link = thisNode.link.link
                else:
                    return None

    # Method to display the elements of the linked list
    def display(self):
        # Display the elements of the linked list
        thisNode = self.head
        while thisNode is not None:
            print(thisNode.data, end=" ")
            thisNode = thisNode.link
        print()

    # Method to get the size (number of elements) of the linked list
    def sizeOf(self):
        # Get the size of the linked list
        size = 0
        thisNode = self.head
        while thisNode is not None:
            thisNode = thisNode.link
            size += 1
        return size

    # Method to update the value of a node at a specific position
    def updateNode(self, data, pos):
        # Update the value of a node at a specific position in the linked list
        position = 1
        thisNode = self.head
        
        # Handle the case where the linked list is not empty
        if self.head is not None:
            # If the position to update is the first node, update its data
            if position == pos:
                thisNode.data = data
            else:
                # Traverse the linked list to find the node at the specified position and update its data
                while thisNode is not None and position + 1 is not pos:
                    position += 1
                    thisNode = thisNode.link
                if thisNode is not None:
                    thisNode.data = data
                else:
                    return False

    # Method to invert the order of nodes in the linked list
    def invert(self):
        # Invert the order of nodes in the linked list
        previousNode = None
        thisNode = self.head
        while thisNode is not None:
            link = thisNode.link
            thisNode.link = previousNode
            previousNode = thisNode
            thisNode = link
        self.head = previousNode

    # Method to concatenate the linked list with another linked list
    def concat(self, list2):
        # Concatenate the current linked list with another linked list
        if list2.head is not None:
            if self.last is not None:
                self.last.link = list2.head
                self.last = list2.last
            else:
                self.head = list2.head
                self.last = list2.last
            list2.head = None
            list2.last = None