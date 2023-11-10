class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right