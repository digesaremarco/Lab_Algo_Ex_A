from ABRNode import Node


class ABR:
    def __init__(self, root=None):
        self.root = root

    def setRoot(self, key):
        self.root = Node(key)

    def add(self, key):
        if self.root is None:
            self.setRoot(key)
        else:
            self.addNode(key, self.root)

    def addNode(self, key, currentNode):
        if key <= currentNode.getValue():
            if currentNode.getLeft() is not None:
                self.addNode(key, currentNode.getLeft())  # recursive call with the left child as the current node
            else:
                currentNode.setLeft(Node(key))
        else:
            if currentNode.getRight() is not None:
                self.addNode(key, currentNode.getRight())  # recursive call with the right child as the current node
            else:
                currentNode.setRight(Node(key))

    def search(self, key):
        if self.root:  # if the tree is not empty
            return self.searchNode(key, self.root)
        else:
            return False

    def searchNode(self, key, currentNode):
        if key == currentNode.getValue():
            return True
        elif key < currentNode.getValue() and currentNode.getLeft() is not None:
            return self.searchNode(key, currentNode.getLeft())
        elif key > currentNode.getValue() and currentNode.getRight() is not None:
            return self.searchNode(key, currentNode.getRight())
        return False  # if the key is not found

    def remove(self, key):
        if self.root:  # if the tree is not empty
            self.removeNode(key, self.root)
        else:
            return False

    def removeNode(self, key, currentNode):
        if key == currentNode.getValue():
            if currentNode.getLeft() is None and currentNode.getRight() is None: # if the node is a leaf
                currentNode = None
            elif currentNode.getLeft() is None: # if the node has only right child
                currentNode = currentNode.getRight()
            elif currentNode.getRight() is None: # if the node has only left child
                currentNode = currentNode.getLeft()
            else: # if the node has both children
                currentNode.setValue(self.findMin(currentNode.getRight()).getValue()) # replace the value of the node with the minimum value of the right subtree
                currentNode.setRight(self.removeNode(currentNode.getValue(), currentNode.getRight())) # remove the node with the minimum value of the right subtree
        elif key < currentNode.getValue() and currentNode.getLeft() is not None:
            currentNode.setLeft(self.removeNode(key, currentNode.getLeft())) # recursive call with the left child as the current node
        elif key > currentNode.getValue() and currentNode.getRight() is not None:
            currentNode.setRight(self.removeNode(key, currentNode.getRight())) # recursive call with the right child as the current node
        return currentNode

    def findMin(self, currentNode):
        if currentNode.getLeft():
            return self.findMin(currentNode.getLeft())
        return currentNode