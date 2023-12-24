# Node class represents a node in the linked list
class Node:
    def __init__(self, neighbor):
        self.neighbor = neighbor  # The neighbor value of the node
        self.next = None  # Reference to the next node in the linked list

# LinkedList class represents a linked list of neighbors for a vertex
class LinkedList:
    def __init__(self):
        self.head = None  # The head of the linked list

    def addEdge(self, neighbor):
        # Add a new edge (node) to the linked list
        newNode = Node(neighbor)
        newNode.next = self.head
        self.head = newNode

    def removeEdge(self, neighbor):
        # Remove an edge (node) from the linked list
        thisNode = self.head
        if thisNode and thisNode.neighbor == neighbor:
            self.head = thisNode.next
            return
        while thisNode.next:
            if thisNode.next.neighbor == neighbor:
                thisNode.next = thisNode.next.next
                return
            thisNode = thisNode.next
            
    def display(self):
        thisNode = self.head
        while thisNode:
            print(f"{thisNode.neighbor} -> ", end='')
            thisNode = thisNode.next
        print("None")

# Graph class represents a graph using an adjacency list
class Graph:
    def __init__(self):
        self.vertex = {}  # Dictionary to store vertices and their linked lists

    def addVertex(self, vertex):
        # Add a new vertex to the graph
        if vertex not in self.vertex:
            self.vertex[vertex] = LinkedList()
            return True
        else:
            return False  # Vertex already exists

    def removeVertex(self, vertex):
        # Remove a vertex and its associated linked list from the graph
        if vertex not in self.vertex:
            return False  # Vertex doesn't exist
        elif vertex in self.vertex:
            del self.vertex[vertex]
            # Remove the vertex from the linked lists of other vertices
            for otherVertex, linkedList in self.vertex.items():
                linkedList.removeEdge(vertex)
            return True

    def addEdge(self, vertex1, vertex2):
        # Add an undirected edge between two vertices
        if vertex1 in self.vertex and vertex2 in self.vertex:
            self.vertex[vertex1].addEdge(vertex2)
            self.vertex[vertex2].addEdge(vertex1)
            return True
        else:
            return False  # One or both vertices don't exist

    def removeEdge(self, vertex1, vertex2):
        # Remove an undirected edge between two vertices
        if vertex1 in self.vertex and vertex2 in self.vertex:
            self.vertex[vertex1].removeEdge(vertex2)
            self.vertex[vertex2].removeEdge(vertex1)
            return True
        else:
            return False  # One or both vertices don't exist
              
    def DFS(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=' ')

        thisNode = self.vertex[start].head
        while thisNode:
            neighbor = thisNode.neighbor
            if neighbor not in visited:
                self.DFS(neighbor, visited)
            thisNode = thisNode.next
           
    def display(self):
        for vertex, linkedList in self.vertex.items():
            print(f"Vertex {vertex}: ", end='')
            linkedList.display()

if __name__ == "__main__":
    graph = Graph()

    for i in range(1, 6):
        graph.addVertex(i)

    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(2, 3)
    graph.addEdge(2, 4)
    graph.addEdge(3, 5)
    graph.addEdge(4, 5)

    print("Original Graph:")
    graph.display()

    print("\nDepth-First Search (DFS):")
    graph.DFS(1)  # Provide the starting vertex for DFS