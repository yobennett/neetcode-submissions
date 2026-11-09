class LinkedList:
    
    def __init__(self):
        self.arr = []

    
    def get(self, index: int) -> int:
        if not self.arr or index < 0 or index >= len(self.arr):
            return -1
        return self.arr[index]

    def insertHead(self, val: int) -> None:
        self.arr = [val] + self.arr
        

    def insertTail(self, val: int) -> None:
        self.arr = self.arr + [val]
        

    def remove(self, index: int) -> bool:
        if not self.arr or index < 0 or index >= len(self.arr):
            return False
        self.arr = self.arr[0:index] + self.arr[index+1:]
        return True

    def getValues(self) -> List[int]:
        return self.arr
