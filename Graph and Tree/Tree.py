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