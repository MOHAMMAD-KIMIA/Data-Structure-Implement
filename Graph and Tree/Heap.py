# Define a generic Heap class
class Heap:
    def __init__(self):
        # Initialize an empty list to represent the heap
        self.heap = []

    def parent(self, i):
        # Calculate the index of the parent of the element at index i
        return (i - 1) // 2

    def leftChild(self, i):
        # Calculate the index of the left child of the element at index i
        return 2 * i + 1

    def rightChild(self, i):
        # Calculate the index of the right child of the element at index i
        return 2 * i + 2

    def compare(self, a, b):
        # Abstract method; subclasses must implement the comparison logic
        raise NotImplementedError("Subclasses must implement the compare method.")

    def swap(self, i, j):
        # Swap elements at indices i and j in the heap
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify(self, i):
        # Maintain the heap property by recursively adjusting elements starting from index i
        l = self.leftChild(i)
        r = self.rightChild(i)
        extreme = i
        # Compare left child with the current extreme
        if l < len(self.heap) and self.compare(self.heap[l], self.heap[extreme]):
            extreme = l
        # Compare right child with the current extreme
        if r < len(self.heap) and self.compare(self.heap[r], self.heap[extreme]):
            extreme = r
        # If a new extreme is found, swap and recursively heapify
        if extreme != i:
            self.swap(i, extreme)
            self.heapify(extreme)

    def insert(self, value):
        # Insert a new element into the heap and maintain the heap property
        self.heap.append(value)
        i = len(self.heap) - 1
        # Move the new element up the tree until the heap property is restored
        while i > 0 and self.compare(self.heap[i], self.heap[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def getExtreme(self):
        # Return the extreme (minimum or maximum) element of the heap
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def extractExtreme(self):
        # Extract the extreme element from the heap and maintain the heap property
        # Check if the heap is empty
        if len(self.heap) == 0:
            return None
        # Get the current extreme element
        extremeVal = self.heap[0]
        # Replace the root with the last element and remove the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # Restore the heap property by heapifying from the root
        self.heapify(0)
        # Return the extracted extreme element
        return extremeVal

    def remove(self, value):
        # Remove a specified value from the heap and maintain the heap property
        # Initialize index variable to track the position of the value to be removed
        i = 0
        # Iterate through the heap to find the position of the specified value
        while i < len(self.heap):
            # Check if the current element is equal to the specified value
            if self.heap[i] == value:
                # Replace the element to be removed with the last element in the heap
                self.heap[i] = self.heap[-1]
                # Remove the last element
                self.heap.pop()
                # Restore the heap property by heapifying from the updated position
                self.heapify(i)
                # Exit the loop once the value is removed
                break
            i += 1

# Define a MinHeap class, inheriting from the Heap class
class MinHeap(Heap):
    def compare(self, a, b):
        # Implement the comparison logic for MinHeap (a < b)
        return a < b

    def build_heap(self, input_list):
        # Build a MinHeap from the given input list
        self.heap = input_list[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)

# Define a MaxHeap class, inheriting from the Heap class
class MaxHeap(Heap):
    def compare(self, a, b):
        # Implement the comparison logic for MaxHeap (a > b)
        return a > b

    def build_heap(self, input_list):
        # Build a MaxHeap from the given input list
        self.heap = input_list[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)
