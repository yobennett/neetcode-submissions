class MinHeap:
    # AKA priority queue
    
    def __init__(self):
        self.heap = [0] # dummy val makes easier using array instead of a tree

        # [0, 1, 2, 3]
        # ex. i=1, left child -> 1*2=2
        # IMPORTANT: how to get parent position, i.e. // 2, watch Heap Props lesson

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1) # use index just pushed

    def pop(self) -> int:
        # no values
        if len(self.heap) == 1:
            return -1
        
        # only one non-dummy value
        if len(self.heap) == 2:
            return self.heap.pop()
        
        # remove root
        #   1) don't remove root
        #   2) move last to the root, keeps structure but not order so bubble down
        # preserve
        root = self.heap[1]
        # move last element -> root
        self.heap[1] = self.heap.pop()
        # bubble down new root
        self._bubble_down(1)

        return root

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums # keep dummy val
        for i in reversed(range(1, len(self.heap) // 2 + 1)): # to skip half of the heap
            self._bubble_down(i)

    # while sorted value is not maintained
    # i.e. maintained -> descendants are larger, ancestors are smaller 
    def _bubble_up(self, index):
        parent = index // 2 # round down
        while index > 1 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = index // 2


    # swap with min(of children), get index of left and right child
    def _bubble_down(self, index):
        child = 2 * index # left -> child, right -> child + 1
        
        # iterate until no children
        while child < len(self.heap):
            # has right child?
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                # right child is smaller
                child += 1

            # short circuit if no need to swap, child is bigger
            if self.heap[child] >= self.heap[index]:
                return

            # swap
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            # move index and update child
            index = child
            child = 2 * index