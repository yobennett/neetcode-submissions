class MedianFinder:
    # Two Heaps
    def __init__(self):
        self.small = [] # max heap (values multiplied by -1)
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        # if large is non-empty and num is larger than curr largest
        # push to large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        # else 
        # push to small
        else:
            heapq.heappush(self.small, -num)

        # too many values in small
        # pop then push to large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # too many values in large
        # pop then push to small
        if len(self.large) > len(self.small) + 1:
            val = -heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        # more values in small
        if len(self.small) > len(self.large):
            return -self.small[0]
        # more values in large
        elif len(self.large) > len(self.small):
            return self.large[0]
        # same number of values in small and large
        else:
            return (-self.small[0] + self.large[0]) / 2.0
        