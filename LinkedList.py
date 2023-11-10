from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp  # insert at the beginning

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:  # search until the end of the list or until the item is found
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:  # if the item is the first in the list
            self.head = current.getNext()
        else:  # if the item is in the middle or at the end
            previous.setNext(current.getNext())

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
