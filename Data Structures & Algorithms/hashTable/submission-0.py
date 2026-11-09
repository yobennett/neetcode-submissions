class Node:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.table = [None] * capacity

    def hash_function(self, key):
        return key % self.cap

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                # found?
                if node.key == key:
                    node.val = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1
        if self.size / self.cap >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]

        while node:
            # found?
            if node.key == key:
                return node.val
            # iterate
            node = node.next

        # not found
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.table[index]
        prev = None

        while node:
            # found
            if node.key == key:
                if prev:
                    # remove non-first 
                    prev.next = node.next
                else:
                    # first
                    self.table[index] = node.next
                self.size -= 1
                return True
            # iterate 
            prev, node = node, node.next

        # not found
        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.cap


    def resize(self) -> None:
        self.cap *= 2
        new_table = [None] * self.cap

        # hash function changes now since cap increased
        for node in self.table:
            # each node is a linked list
            while node:
                index = node.key % self.cap
                # no nodes yet
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.val)
                # already has nodes, insert at the end of the linked list
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.val)

                # iterate
                node = node.next

        self.table = new_table
