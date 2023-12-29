class BinaryTree:
    # Inner class representing a tree node
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    # Constructor for the BinaryTree class
    def __init__(self):
        self.root = None  # Initialize the root of the tree to None
            
    # Recursive method to insert a value into the tree
    def insertRec(self, root, val):
        if root is None:
            return self.TreeNode(val)  # Create a new node if the current node is None
        if val < root.data:
            root.left = self.insertRec(root.left, val)  # Recursively insert into the left subtree
        elif val > root.data:
            root.right = self.insertRec(root.right, val)  # Recursively insert into the right subtree
        return root
    
    # Public method to insert a value into the tree
    def insert(self, val):
        self.root = self.insertRec(self.root, val)

    # Helper function to find the rightmost node in the left subtree
    def rightMin(self, root):
        temp = root
        while temp.left is not None:
            temp = temp.left
        return temp.data

    # Recursive method to remove a value from the tree
    def removeBST(self, root, val):
        if root is None:
            return None

        if root.data < val:
            root.right = self.removeBST(root.right, val)

        elif root.data > val:
            root.left = self.removeBST(root.left, val)

        else:
            if root.left is None and root.right is None:
                del root
                return None
            elif root.left is None:
                temp = root.right
                del root
                return temp
            elif root.right is None:
                temp = root.left
                del root
                return temp
            else:
                rightMin = self.rightMin(root.right)
                root.data = rightMin
                root.right = self.removeBST(root.right, rightMin)
        return root        
    
    def search(self, val):
        return self.searchRec(self.root, val)

    # Recursive method to search for a value in the tree
    def searchRec(self, root, val):
        if root is None or root.data == val:
            return root
        if val < root.data:
            return self.searchRec(root.left, val)
        return self.searchRec(root.right, val)
    
    # Recursive method to print the tree in inorder traversal
    def printInorder(self, root):
        if root is not None:
            self.printInorder(root.left)  # Recursively print the left subtree
            print(root.data, end=" ")  # Print the current node
            self.printInorder(root.right)  # Recursively print the right subtree

    # Public method to print the tree in inorder traversal
    def inOrder(self):
        self.printInorder(self.root)
        
    def printPreorder(self, root):
        if root is not None:
            print(root.data, end=' ')  # Print the current node
            self.printPreorder(root.left)  # Recursively print the left subtree
            self.printPreorder(root.right)  # Recursively print the right subtree
            
    def preOrder(self):
        self.printPreorder(self.root)
    
    def printPostorder(self, root):
        if root is not None:
            self.printPostorder(root.left)  # Recursively print the left subtree
            self.printPostorder(root.right)  # Recursively print the right subtree
            print(root.data, end=' ')  # Print the current node
            
    def postOrder(self):
        self.printPostorder(self.root)