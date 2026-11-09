class SegmentTree:

    def __init__(self, startTime: int, endTime: int):
        self.left = None
        self.right = None
        self.startTime = startTime
        self.endTime = endTime

    def insert(self, startTime, endTime):
        curr = self
        while True:
            if startTime >= curr.endTime:
                if not curr.right:
                    curr.right = SegmentTree(startTime, endTime)
                    return True
                curr = curr.right
            elif endTime <= curr.startTime:
                if not curr.left:
                    curr.left = SegmentTree(startTime, endTime)
                    return True
                curr = curr.left
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
        return self.root.insert(startTime, endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)