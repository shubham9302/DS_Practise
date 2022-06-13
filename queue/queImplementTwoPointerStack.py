class QueData:
    def __init__(self, size=None):
        self.queData = []
        self.size = size
        self.rear = -1
        self.front = -1

    def enque(self, value):
        if self.rear < self.size:
            self.rear += 1
            self.queData.append(value)
        else:
            raise Exception("Max size reached")

    def deque(self):
        if self.front != self.rear:
            self.front += 1
            del self.queData[self.front]
            self.rear -= 1
        elif self.isEmpty():
            raise Exception("Que is Empty")

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def printQue(self):
        print(*self.queData)

    def isFull(self):
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
    t1.deque()
    t1.printQue()
    t1.enque(3)
    t1.enque(-1)
    t1.enque(-2)
    t1.printQue()
    #t1.deque()
    t1.printQue()
    print(t1.rear)
    print(t1.isFull())

### Time complexity
## enque -> O(1)
## deque -> O(1)
