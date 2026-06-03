class DynamicArray:
    
    arr = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        popped = self.arr[self.size - 1]
        self.arr[self.size - 1] = 0
        self.size -= 1
        return popped

    def resize(self) -> None:
        new_empty = [0] * self.capacity
        self.arr.extend(new_empty)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
