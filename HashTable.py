class HashTable:
    def __init__(self, nitems):
        self.size = nitems/0.8 # the size of the table is 20% bigger than the number of items, it gives a load factor of 0.8
        self.table = [None] * self.size  # create an empty list

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
