class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.arr = []

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()
        self.arr.append(n)
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr.pop()

    def resize(self) -> None:
        self.cap *= 2

    def getSize(self) -> int:
        return self.size        
    
    def getCapacity(self) -> int:
        return self.cap
