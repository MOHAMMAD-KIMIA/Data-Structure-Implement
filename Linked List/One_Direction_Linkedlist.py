class Node:
    def __init__(self, data):
        # Initialize a new Node with the given data and a null link
        self.data = data
        self.link = None

class linkedList:
        
    def __init__(self):
        # Initialize a new linked list with a null head
        self.head = None
        self.last = None
        
    def insertAtfirst(self, data):
        # Insert a new node at the beginning of the linked list
        newNode = Node(data)
        
        # If the linked list is empty, set the head to the new node
        if self.head is None:
            self.head = newNode
            return
        # If the linked list is not empty, set the new node's link to the current head and update the head
        else:
            newNode.link = self.head
            self.head = newNode
            
    def insertAtend(self, data):
        # Insert a new node at the end of the linked list
        newNode = Node(data)
        newNode.link = None
        thisNode = self.head
        
        # If the linked list is empty, return the new node
        if self.head == None:
            return newNode
        # Iterate through the linked list to find the last node and append the new node
        while thisNode.link is not None:
            thisNode = thisNode.link
        thisNode.link = newNode
        return self.head
        
    def insertWherever(self, data, pos):
        # Insert a new node at a specific position in the linked list
        newNode = Node(data)
        position = 1
        thisNode = self.head
        
        # Handle the case where the linked list is empty
        if position == pos:
            self.insertAtfirst = newNode
        # Handle the case where the linked list is not empty
        else:
            # Search for the index in the linked list
            while thisNode is not None and position+1 is not pos:
                position = position + 1
                thisNode = thisNode.link
            # When the position is found, insert the new node at that position
            if thisNode is not None:
                newNode.link = thisNode.link
                thisNode.link = newNode
            # When the position is not found, return False
            else:
                return False

    def deleteFromfirst(self):
        # Check if the linked list is empty
        if self.head == None:
            return self.data
        # Move the head pointer to the next node
        else:
            self.head = self.head.link
            
    def deleteFromlast(self):
        # Check if the linked list is empty
        if self.head == None:
            return False
        # Traverse the linked list to find the second last node and set its link to None
        thisNode = self.head
        while thisNode.link.link is not None:
            thisNode = thisNode.link
        thisNode.link = None
        
    def deletWherever(self, pos):
        # Initialize position and thisNode
        position = 1
        thisNode = self.head
        # Check if the linked list is empty
        if self.head == None:
            return False
        # If the position to delete is the first node, call deleteFromfirst()
        elif position == pos:
            self.deletFromfirst()
        # Traverse the linked list to find the node at the specified position and delete it
        else:
            while thisNode is not None and position+1 is not pos:
                position = position + 1
                thisNode = thisNode.link
            if thisNode is not None:
                thisNode.link = thisNode.link.link
            else:
                return self.data
            
    def display(self):
        # Initialize thisNode as the head
        thisNode = self.head
        # Traverse the linked list and print the data of each node
        while thisNode is not None:
            print(thisNode.data)
            thisNode = thisNode.link
            
    def sizeOf(self):
        # Initialize size as 0
        size = 0
        # Check if the linked list is not empty
        if self.head is not None:
            # Traverse the linked list and count the nodes
            thisNode = self.head
            while thisNode is not None:
                thisNode = thisNode.link
                size += 1
            return size
        else:
            return 0
    
    def updateNode(self, data, pos):
        # Initialize position and thisNode
        position = 0
        thisNode = self.head
        # Check if the linked list is empty
        if position == pos:
            # Update the data of the first node
            thisNode.data = data
        else:
            # Traverse the linked list to find the node at the specified position and update its data
            while thisNode is not None and position+1 is not pos:
                position = position + 1
                thisNode = thisNode.link
            if thisNode is not None:
                thisNode.data = data
            else:
                return False

    def invert(self):
        # Initialize previosNode as None and thisNode as the head
        previosNode = None
        thisNode = self.head
        # Traverse the linked list and reverse the links of the nodes
        while (thisNode is not None):
            link = thisNode.link
            thisNode.link = previosNode
            previosNode = thisNode
            thisNode = link
        # Set the head to the last node (previosNode)
        self.head = previosNode

    def concat(self, list2):
        if list2.head is not None:
            if self.last is not None:
                self.last.link = list2.head
                self.last = list2.last
            else:
                self.head = list2.head
                self.last = list2.last
            list2.head = None
            list2.last = None
