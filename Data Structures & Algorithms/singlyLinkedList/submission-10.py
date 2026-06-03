class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        # [a,b] a = current, b = next
        self.size = 0
        self.head = None
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        i=0
        curr = self.head
        while i != index:
            curr = curr.next
            i+=1
        return curr.val

    def insertHead(self, val: int) -> None:
        old = self.head
        self.head = Node(val, old)
        self.size += 1

    def insertTail(self, val: int) -> None:
        curr = self.head
        if not curr:
            self.insertHead(val)
        else:
            while curr.next:
                curr = curr.next
            curr.next = Node(val)
            self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -=1
        return True
            


    def getValues(self) -> List[int]:
        curr = self.head
        if curr:
            vals = [curr.val]
            while curr.next:
                curr = curr.next
                vals.append(curr.val)
            return vals
        else:
            return []