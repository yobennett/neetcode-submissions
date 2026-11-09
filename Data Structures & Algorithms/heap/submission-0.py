import heapq

class MinHeap:
    
    def __init__(self):
        self.minHeap = []
        

    def push(self, val: int) -> None:
        heapq.heappush(self.minHeap, val)

    def pop(self) -> int:
        if len(self.minHeap) > 0:
            return heapq.heappop(self.minHeap)
        return -1

    def top(self) -> int:
        if len(self.minHeap) > 0:
            return self.minHeap[0]
        return -1
        

    def heapify(self, nums: List[int]) -> None:
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        