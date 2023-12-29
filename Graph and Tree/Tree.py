class TreeLinkedList:
    # Inner class representing a tree node
    class Tree:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None

    # Constructor for the TreeLinkedList class
    def __init__(self):
        self.root = None  # Initialize the root of the tree to None

    # Public method to insert a value into the tree
    def insert(self, data):
        self.root = self.insertRec(self.root, data)

    # Private recursive method to insert a value into the tree
    def insertRec(self, root, data):
        if root is None:
            return self.Tree(data)  # Create a new node if the current node is None

        if data < root.data:
            root.left = self.insertRec(root.left, data)  # Recursively insert into the left subtree
        elif data > root.data:
            root.right = self.insertRec(root.right, data)  # Recursively insert into the right subtree

        return root

    # Public method to remove a value from the tree
    def remove(self, data):
        self.root = self.removeRec(self.root, data)

    # Private recursive method to remove a value from the tree
    def removeRec(self, root, data):
        if root is None:
            return None

        if data < root.data:
            root.left = self.removeRec(root.left, data)
        elif data > root.data:
            root.right = self.removeRec(root.right, data)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            root.data = self.minVal(root.right).data
            root.right = self.removeRec(root.right, root.data)

        return root

    # Helper method to find the node with the minimum value in a subtree
    def minVal(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    # Display the entire tree
    def displayTree(self):
        h = self.height(self.root)  # Get the height of the tree
        for i in range(1, h+1):
            self.traverse(self.root, i)  # Traverse and print each level of the tree

    # Perform an in-order traversal of the tree
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)  # Traverse the left subtree
            print(root.data, end=" ")  # Print the current node's data
            self.inOrder(root.right)  # Traverse the right subtree

    # Perform a post-order traversal of the tree
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)  # Traverse the left subtree
            self.postOrder(root.right)  # Traverse the right subtree
            print(root.data, end=" ")  # Print the current node's data

    # Perform a pre-order traversal of the tree
    def preOrder(self, root):
        if root:
            print(root.data, end=" ")  # Print the current node's data
            self.preOrder(root.left)  # Traverse the left subtree
            self.preOrder(root.right)  # Traverse the right subtree

    # Calculate the height of the tree
    def height(self, root):
        if not root:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        # Return the maximum height of the left and right subtrees, plus 1 for the current level
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

    # Traverse and print nodes at a specific level of the tree
    def traverse(self, root, level):
        if not root:
            return
        if level == 1:
            print(root.data, end=" ")  # Print the data of the current node
        elif level > 1:
            self.traverse(root.left, level - 1)  # Traverse the left subtree
            self.traverse(root.right, level - 1)  # Traverse the right subtree