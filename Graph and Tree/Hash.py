class Node:
    def __init__(self, key, value):
        # Node constructor to create a new node with key, value, and next pointer
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=10):
        # HashTable constructor with an optional capacity, default is 10
        self.capacity = capacity
        # Initialize the table as a list of 'None' elements
        self.table = [None] * capacity

    def hashFunc(self, key):
        # A simple hash function for strings, summing ASCII values
        return sum(ord(char) for char in key) % self.capacity

    def insert(self, key, value):
        # Get the index using the hash function
        index = self.hashFunc(key)
        # Create a new node
        new_node = Node(key, value)

        # If the bucket is empty, insert the new node
        if not self.table[index]:
            self.table[index] = new_node
        else:
            # If the bucket is not empty, traverse the linked list to find the end
            current = self.table[index]

            while current.next:
                # Update the value if the key already exists in the list
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            # Insert the new node at the end of the linked list
            current.next = new_node

    def remove(self, key):
        # Get the index using the hash function
        index = self.hashFunc(key)
        current = self.table[index]
        previous = None

        # Traverse the linked list to find the node with the given key
        while current:
            if current.key == key:
                # If the node is found, remove it from the linked list
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return

            previous = current
            current = current.next

        # Raise an error if the key is not found
        raise KeyError(key)

    def sizeOf(self):
        # Calculate the size of the hash table by counting non-empty buckets
        return sum(1 for bucket in self.table if bucket)

    def search(self, key):
        # Get the index using the hash function
        index = self.hashFunc(key)
        current = self.table[index]

        # Traverse the linked list to find the node with the given key
        while current:
            if current.key == key:
                # Return the value if the key is found
                return current.value
            current = current.next

        # Raise an error if the key is not found
        raise KeyError(key)

    def hasKey(self, key):
        # Get the index using the hash function
        index = self.hashFunc(key)
        # Return the index, not a boolean indicating whether the key exists
        return index