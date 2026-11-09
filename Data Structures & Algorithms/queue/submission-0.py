class Deque:
    
    def __init__(self):
        self.arr = collections.deque()

    def isEmpty(self) -> bool:
        if len(self.arr) == 0:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        self.arr.append(value)

    def appendleft(self, value: int) -> None:
        self.arr.appendleft(value)

    def pop(self) -> int:
        # empty
        if self.isEmpty():
            return -1
        return self.arr.pop()

    def popleft(self) -> int:
        # empty
        if self.isEmpty():
            return -1
        return self.arr.popleft()