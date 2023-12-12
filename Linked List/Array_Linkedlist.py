from One_Direction_Linkedlist import linkedList

class Array:
    array = linkedList.LinkedList()
    
    def add(self, data, position):
        self.array.insertWherever(data, position)
            
    def delete(self, position):
        return self.array.deletWherever(position)
    
    def size(self):
        return self.array.sizeOf()
            
    def display(self):
        self.array.display()