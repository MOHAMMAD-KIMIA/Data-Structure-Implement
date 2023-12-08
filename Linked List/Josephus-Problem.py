class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def josephus(n, k):
    
    # declared Node
    head = Node(1)
    ptr = head
    
    # Create a circular linked list with n nodes
    # Start from 2 because we have the first Node 
    for i in range(2, n+1):
        newNode = Node(i)
        ptr.next = newNode
        newNode.next = head
        ptr = newNode
    
    # Remove every k-th node until only one node remains
    count = n
    while count > 1:
        for i in range(k-1):
            ptr = ptr.next
        ptr.next = ptr.next.next
        count -= 1
    
    # Return the data of the remaned node
    return ptr.next.data

n = int(input())
k = int(input())
print(josephus(n, k))