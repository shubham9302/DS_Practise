class QueData:
    def __init__(self, size=None):
        self.queData = [None] * size
        self.size = size
        self.rear = 0
        self.front = 0

    def enque(self, value):
        if self.rear < self.size - 1 and not self.isFull():
            self.rear += 1
            self.queData[self.rear] = value
        elif not self.isEmpty() and self.endReached():
            self.rear = 0
            self.queData[self.rear] = value
        elif self.isFull():
            raise Exception("Max size reached")

    def deque(self):
        if self.front != self.rear:
            self.front += 1
            value = self.queData[self.front]
            return value
        elif self.isEmpty():
            return "Que is empty"

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def printQue(self):
        print(*self.queData)

    def isFull(self):
        if self.rear == self.front - 1:
            return True
        return False

    def endReached(self):
        if self.rear == self.size - 1:
            return True
        return False


if __name__ == "__main__":
    t1 = QueData(5)
    # t1.deque()
    t1.enque(2)
    t1.enque(3)
    t1.enque(-1)
    t1.printQue()
    print("front", t1.front)
    t1.deque()
    t1.printQue()
    t1.enque(-33)
    t1.printQue()
    t1.enque(-11)
    t1.deque()
    print("front", t1.front)
    t1.printQue()
    t1.enque(-22)
    print(t1.front)
    t1.printQue()
    t1.deque()
    print("deque result")
    t1.printQue()

    t1.enque(-4)
    t1.printQue()
    print(t1.rear)
    print(t1.isFull())

### Time complexity
## enque -> O(1)
## deque -> O(1)
