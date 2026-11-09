class SegmentTree:
    # simplified SegmentTree, build only one insert at a time
    def __init__(self, startTime: int, endTime: int):
        self.left = None
        self.right = None
        self.startTime = startTime
        self.endTime = endTime

    def insert(self, startTime, endTime):
        curr = self
        while True:
            # new booking starts at/after current end
            if startTime >= curr.endTime:
                if not curr.right:
                    # initialize right tree with new booking
                    curr.right = SegmentTree(startTime, endTime)
                    return True
                curr = curr.right
            # new booking ends at/before current start
            elif endTime <= curr.startTime:
                if not curr.left:
                    # initialize left tree with new booking
                    curr.left = SegmentTree(startTime, endTime)
                    return True
                curr = curr.left
            # new booking can't be inserted without overlapping any of the node's start and end
            else:
                return False
        return True



class MyCalendar:
    
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = SegmentTree(startTime, endTime)
            return True
        # False if double-books
        return self.root.insert(startTime, endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)