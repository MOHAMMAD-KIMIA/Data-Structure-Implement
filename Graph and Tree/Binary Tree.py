class BinaryTree:
    # Inner class representing a tree node
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.height = 1
    
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
        
class AVL(BinaryTree):
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.height = 1 
            
    def insertAVL(self, val):
        self.root = self.insertRec(self.root, val)
        self.root = self.balance(self.root)
        
    def removeAVL(self, val):
        self.root = self.removeBST(self.root, val)
        self.root = self.balance(self.root)
    
    def height(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def balanceFactor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def leftRotate(self, y):
        # Store the right child of y in x
        x = y.right
        # Make the left child of x the new right child of y
        y.right = x.left
        # Make y the left child of x
        x.left = y

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        # Return the new root of the balanced subtree
        return x

    def rightRotate(self, y):
        # Store the left child of y in x
        x = y.left
        # Make the right child of x the new left child of y
        y.left = x.right
        # Make y the right child of x
        x.right = y

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        # Return the new root of the balanced subtree
        return x
    
    def balance(self, node):
        if node is None:
            return None

        # Update height of the current node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Check balance factor
        balanceFactor = self.balanceFactor(node)

        # Left Heavy
        if balanceFactor > 1:
            # Left-Right Case
            if self.balanceFactor(node.left) < 0:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Right Heavy
        if balanceFactor < -1:
            # Right-Left Case
            if self.balanceFactor(node.right) > 0:
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node