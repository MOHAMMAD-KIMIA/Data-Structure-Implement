class Node:
    def __init__(self, val):
        # Initialize a new node with a given value
        self.val = val
        # Initialize parent pointer to None
        self.parent = None
        # Initialize left child pointer to None
        self.left = None
        # Initialize right child pointer to None
        self.right = None
        # Initialize node color to red (1) by default; 0 represents black
        self.color = 1


class RB_Tree:
    def __init__(self):
        # Create a null node with color black
        self.null = Node(0)
        self.null.color = 0
        self.null.left = None
        self.null.right = None
        # Initialize an empty Red-Black Tree with root pointing to the null node
        self.root = self.null

    # Insert a new node with a given key into the Red-Black Tree
    def insertNode(self, key):
        newNode = Node(key)
        newNode.parent = None
        newNode.val = key
        newNode.left = self.null
        newNode.right = self.null
        newNode.color = 1  # Initially set the new node's color to red

        y = None
        x = self.root

        # Find the new node's position in the tree
        while x != self.null:
            y = x
            if newNode.val < x.val:
                x = x.left
            else:
                x = x.right

        newNode.parent = y

        # Update parent's left or right child pointer based on the new node's value
        if y is None:
            self.root = newNode  # If parent is None, the new node becomes the root
        elif newNode.val < y.val:
            y.left = newNode
        else:
            y.right = newNode

        if newNode.parent is None:
            newNode.color = 0  # Set color to black for the root
            return

        if newNode.parent.parent is None:
            return

        self.fixInsert(newNode)  # Fix the Red-Black Tree after insertion

    # Left rotation operation on the Red-Black Tree
    def leftRotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.null:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # Right rotation operation on the Red-Black Tree
    def rightRotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.null:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # Fix the Red-Black Tree after insertion
    def fixInsert(self, k):
        while k.parent.color == 1:  # If parent's color is red
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:  # If uncle is red
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rightRotate(k)

                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.leftRotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:  # If uncle is red
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.leftRotate(k)

                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rightRotate(k.parent.parent)

            if k == self.root:  # If the current node is the root
                break

        self.root.color = 0  # Set color to black for the root

    # Fix the Red-Black Tree after deletion
    def fixDelete(self, x):
        while x != self.root and x.color == 0:  # If the current node is black and not the root
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:  # If sibling is red
                    s.color = 0
                    x.parent.color = 1
                    self.leftRotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:  # If both children of the sibling are black
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:  # If the right child of the sibling is black
                        s.left.color = 0
                        s.color = 1
                        self.rightRotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.leftRotate(x.parent)
                    x = self.root

            else:
                s = x.parent.left
                if s.color == 1:  # If sibling is red
                    s.color = 0
                    x.parent.color = 1
                    self.rightRotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:  # If both children of the sibling are black
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:  # If the left child of the sibling is black
                        s.right.color = 0
                        s.color = 1
                        self.leftRotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rightRotate(x.parent)
                    x = self.root

        x.color = 0  # Set color to black for the final node

    # Transplanting nodes in the Red-Black Tree
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    # Find the minimum value node in the Red-Black Tree
    def minimum(self, node):
        while node.left != self.null:
            node = node.left

        return node

    # Delete a node with a given key in the Red-Black Tree
    def delete(self, node, key):
        z = self.null

        while node != self.null:
            if node.val == key:
                z = node

            if node.val <= key:
                node = node.right
            else:
                node = node.left

        if z == self.null:
            print("Error: Node with key", key, "not found.")
            return

        y = z
        yOriginalColor = y.color

        if z.left == self.null:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.null:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            yOriginalColor = y.color
            x = y.right

            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if yOriginalColor == 0:
            self.fixDelete(x)  # Fix the Red-Black Tree after deletion

    # Delete a node with a given key in the Red-Black Tree (wrapper function)
    def deleteNode(self, val):
        self.delete(self.root, val)

    # Display the Red-Black Tree
    def display(self):
        if self.root != self.null:
            self.displayHelper(self.root)
        else:
            print("Empty Tree")

    # Helper method for in-order traversal and display
    def displayHelper(self, node):
        if node != self.null:
            color_str = "Red" if node.color == 1 else "Black"
            print(f"Node: {node.val}, Color: {color_str}")

            if node.left != self.null:
                print(f"  Left Child: {node.left.val}")
            else:
                print("  Left Child: None")

            if node.right != self.null:
                print(f"  Right Child: {node.right.val}")
            else:
                print("  Right Child: None")

            print("---")

            self.displayHelper(node.left)
            self.displayHelper(node.right)