# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.dequeue = deque()
        self.k = k
    def insertFront(self, value: int) -> bool:
        if len(self.dequeue) < self.k:
            self.dequeue.appendleft(value)
            return True
        return False
    def insertLast(self, value: int) -> bool:
        if len(self.dequeue) < self.k:
            self.dequeue.append(value)
            return True
        return False
    def deleteFront(self) -> bool:
        if len(self.dequeue) != 0:
            self.dequeue.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.dequeue) != 0:
            self.dequeue.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.dequeue) != 0:
            return self.dequeue[0]
        return -1
        

    def getRear(self) -> int:
        if len(self.dequeue) != 0:
            return self.dequeue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.dequeue) == 0
       
    def isFull(self) -> bool:
        return len(self.dequeue) == self.k
           
