class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        
class circularLinkedlist:
    def __init__(self):
        self.head = None
        self.last = None
        
    def insertAtfirst(self, data):
        newNode = Node(data)
        
        if self.last is None:
            self.last = newNode
            self.last.link = self.last
            return self.last
        
        else:
            newNode.link = self.last.link
            self.last.link = newNode
            return self.last
                     
    def insertAtend(self, data):
        newNode = Node(data)
        if self.last is None:
            self.last = newNode
            self.last.link = self.last
            return self.last
        
        else:
            newNode.link = self.last.link
            self.last.link = newNode
            self.last = newNode
            return self.last
             
    def insertWherever(self, data, x):
        if self.last == None:
            return None

        newNode = Node(data)
        thisNode = self.last.link
        while thisNode:
            if thisNode.data == x:
                newNode.link = thisNode.link
                thisNode.link = newNode
                if thisNode == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            thisNode = thisNode.link
            if thisNode == self.last.link:
                break

    def deleteFirst(self):
        if self.last == None:
            return False
        elif(self.last != None):
            if(self.last.link == self.last):
                self.last = None
            
            else:
                temp = self.last
                while(temp.link != self.last):
                    temp = temp.link
                self.last = self.last.link
                temp.link = self.last 
            
    def deleteLast(self):
        if self.last == None:
            return False
        elif(self.last != None):
            if(self.last.link == self.last):
                self.last = None
            else:
                temp = self.last
                while(temp.link.link != self.last):
                    temp = temp.link
                temp.link = self.last
            
    def deleteWherever(self, x):
        if self.last == None:
            return False
        
        if self.last.link.data == x and self.last.link == self.last:
            self.last = None
        
        thisNode = self.last
        if thisNode.data == x:
            while (thisNode.link != self.last):
                thisNode = thisNode.link
            thisNode.link = self.last.link
            self.last = self.last.link
            return 
        
        while (self.last.link != self.last and self.last.link.data != x):
            thisNode = thisNode.link
        
        if self.last.link.data == x:
            temp = self.last.link
            self.last = temp.link
            temp = None
            
        else:
            return False            
            
    def display(self):
        if self.last == None:
            return False

        thisNode = self.last.link
        while thisNode:
            print(thisNode.data, end=" ")
            thisNode = thisNode.link
            if thisNode == self.last.link:
                break
            
    def sizeOf(self):
        size = 1
        if self.last is not None:
            thisNode = self.last
            while thisNode.link is not self.last:
                thisNode = thisNode.link
                size += 1
                if thisNode == self.head:
                    break
            return size
        else:
            size = 0
            return size
    
    def update(self, data, pos):
        temp = self.head
        for i in range(pos):
            temp = temp.link
        temp.data = data
  
    def concat(self, list2):
        self.size += list2.sizOf()
        if list2.head is not None:
            if self.head is not None:
                self.last.link = list2.head
                self.last = list2.last
                self.last.link = self.head
            else:
                self.head = list2.head
                self.last = list2.last
                self.last.link = self.head

            list2.head = None
            list2.last = None
        
    def invert(self):
        if self.head is None or self.head.link is None:
            return

        previous = None
        thisNode = self.head
        newNode = None

        while thisNode is not None:
            newNode = thisNode.link
            thisNode.link = previous
            previous = thisNode
            thisNode = newNode

        self.head = previous
        self.last.link = self.head
