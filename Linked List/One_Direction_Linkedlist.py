class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        
class linkedList:
    def __init__(self):
        self.head = None
        
    def insertAtfirst(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            return
        
        else:
            newNode.link = self.head
            self.head = newNode
            
    def insertAtend(self, data):
        newNode = Node(data)
        
        # the linked list is empty
        if self.head is None:
            self.head = newNode
            return
        
        thisNode = self.head
        while thisNode.link is not None:
            thisNode = thisNode.link
            
        thisNode.link = newNode
        
    def insertWherever(self, data, pos):
        newNode = Node(data)
        position = 0
        thisNode = self.head
        
        # the linked list is empty
        if position == pos:
            self.insertAtfirst = newNode
        
        # the linked list isn't empty
        else:
            # search for the index in the linked list
            while thisNode is not None and position+1 is not pos:
                position = position + 1
                thisNode = thisNode.link
            
            # when the pos is found
            if thisNode is not None:
                newNode.link = thisNode.link
                thisNode.link = newNode
            
            # when the pos is not found
            else:
                return False

    def deleteFromfirst(self):
        if self.head == None:
            return self.data
        
        else:
            self.head = self.head.link
            
    def deleteFromlast(self):
        if self.head == None:
            return self.data
        
        # check if the two next node's link is Null or not
        thisNode = self.head
        while thisNode.link.link is not None:
            thisNode = thisNode.link
        # if the two next node's link is Null then we change its pointer to Null
        thisNode.link = None
        
    def deletWherever(self, pos):
        position = 0
        thisNode = self.head
        
        if self.head == None:
            return False
        
        elif position == pos:
            self.deletFromfirst()
        
        else:
            while thisNode is not None and position+1 is not pos:
                position = position + 1
                thisNode = thisNode.link
            
            if thisNode is not None:
                thisNode.link = thisNode.link.link
            
            else:
                return self.data
            
    def display(self): 
        thisNode = self.head
        while thisNode is not None:
            print(thisNode.data)
            thisNode = thisNode.link
            
    def sizeOf(self):
        size = 0
        if self.head is not None:
            thisNode = self.head
            while thisNode is not None:
                thisNode = thisNode.link
                size += 1
            return size
        else:
            return 0
    
    def updateNode(self, data, pos):
        position = 0
        thisNode = self.head
        
        # the linked list is empty
        if position == pos:
            thisNode.data = data
            
        else:
            
            while thisNode is not None and position+1 is not pos:
                position = position + 1
                thisNode = thisNode.link
                
            if thisNode is not None:
                thisNode.data = data
            
            else:
                return False
            
    def addTwoList(self, addedList):
        thisNode = self.head
        while thisNode is not None:
            thisNode = thisNode.link
        
        thisNode.link = addedList
        addedList = None
        
    def invert(self):
        previos = None
        thisNode = self.head
        
        while thisNode is not None:
            link = thisNode.link
            thisNode.link = previos
            previos = thisNode
            thisNode = link
            
        self.head = thisNode