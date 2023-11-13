class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # create an empty list of size 'size'

    def hashfunction(self, key, i):
        return (key % self.size + i) % self.size

    def insert(self, key):
        i = 0
        while i < self.size:
            j = self.hashfunction(key, i)
            if self.table[j] is None or self.table[j] == -1:
                self.table[j] = key
                return j
            else:
                i += 1
        return None

    def search(self, key):
        i = 0
        while i < self.size or self.table[j] is not None or self.table[j] != -1: # search until the end of the table or until an empty cell is found
            j = self.hashfunction(key, i)
            if self.table[j] == key:
                return j
            i += 1
        return None

    def remove(self, key):
        j = self.search(key)
        if j is not None:
            self.table[j] = -1  # -1 is a special value that indicates that the cell is deleted
            return True
        else:
            return False
