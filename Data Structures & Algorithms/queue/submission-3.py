class Node:
    def __init__(self, val, next=None, prev=None):
        self.prev = prev
        self.val = val
        self.next = next
        
class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return not self.head and not self.tail

    def append(self, value: int) -> None:
        newNode = Node(value)
        
        if (self.isEmpty()):
            self.head = newNode
            self.tail = newNode
        else:
            previousLastNode = self.tail
            previousLastNode.next = newNode
            newNode.prev = previousLastNode
            self.tail = newNode


    def appendleft(self, value: int) -> None:
        newNode = Node(value)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            previousFirstNode = self.head
            previousFirstNode.prev = newNode
            newNode.next = previousFirstNode
            self.head = newNode

    def pop(self) -> int:
        if not self.tail:
            return -1
        
        poppedVal = self.tail.val
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return poppedVal
        else:
            secondLastNode = self.tail.prev
            secondLastNode.next = None
            self.tail = secondLastNode
            return poppedVal
        

    def popleft(self) -> int:
        if not self.head:
            return -1
        poppedVal = self.head.val

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return poppedVal
        else:
            secondNode = self.head.next
            secondNode.prev = None
            self.head = secondNode
            return poppedVal
        
