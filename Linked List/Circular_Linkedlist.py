class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        
class circularLinkedlist:
    def __init__(self):
        self.head = None
        self.end = None
        
    def insertAtfirst(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.head.link = self.head
            return
        
        else:
            newNode.link = self.head
            self.head = newNode
            self.end.link = self.head
            
    def insertAtend(self, data):
        
        # the linked list is empty
        if self.head is None:
            self.insertAtfirst(data)
        
        else:
            newNode = Node(data)
            newNode.link = self.end.link
            self.end.link = newNode
            self.end = newNode
             
    def insertWherever(self, data, pos):
        newNode = Node(data)
        checkNext = self.end.link
        
        # the linked list is empty
        if self.head is None:
            self.insertAtfirst(data)
        
        # the linked list isn't empty
        else:
            # search for the index in the linked list
            while checkNext is not None:
                if checkNext.data == pos:
                    newNode.link = checkNext.link
                    checkNext.link = newNode
                    
                    if pos == self.end:
                        self.end = checkNext.link

                newNode = newNode.link
            # when the pos is not found
                if newNode == self.end.link:
                    return False

    def deleteFromfirst(self):
        if self.head == None:
            return self.data
        
        else:
            self.head = self.head.link
            self.end.link = self.head
            
    def deleteFromlast(self):
        thisNode = self.head
        
        if self.head == None:
            return self.data
        
        elif self.head.link == self.head:
            self.head = None
            
        else: 
            while thisNode.link.link is not self.end:
                thisNode = thisNode.link
            thisNode.link = self.end
            
    def deleteAtposition(self, pos):
        if self.head is None:
            return None
        
        if pos == 1:
            self.head.data = self.head.link.data
            temp = self.head.link
            self.head.link = self.head.link.link
            del temp
            return self.head
        
        thisNode = self.head
        for i in range(pos - 2):
            thisNode = thisNode.link
        temp = thisNode.link
        thisNode.link = thisNode.link.link
        del temp
        return self.head
            
    def display(self): 
        thisNode = self.head
        while thisNode is not None:
            print(thisNode.data, end=" ")
            thisNode = thisNode.link
            if thisNode == self.head:
                break
        print()
            
    def sizeOf(self):
        size = 0
        if self.head is not None:
            thisNode = self.head
            while thisNode is not None:
                thisNode = thisNode.link
                size += 1
                if thisNode == self.head:
                    break
            return size
        else:
            return 0
    
    def updateData(self, oldData, newData):
        position = 0
        
        if self.head is None:
            return False
        
        thisNode = self.head
        while thisNode.link != self.head:
            if thisNode.data == oldData:
                thisNode.data = newData
                return
            
            thisNode = thisNode.link
            position += 1
        
        if thisNode.link == self.head and thisNode.data != oldData:
            return False
        
    def AddTwoList(self, addedList):
        temp = self.head
        self.head.link = addedList.head.link
        addedList.head.link = temp
        
    def invert(self):
        
        if self.head is not None:
            previous = self.head
            temp = self.head
            thisNode = self.head.link

            previous.link = previous

            while thisNode != self.head:
                temp = thisNode.link
                thisNode.link = previous
                self.head.link = thisNode
                previous = thisNode
                thisNode = temp

            self.head = previous