class QueData:
    def __init__(self, size=None):
        self.queData = []
        self.size = size
        self.rear = None
        self.front = None

    def enque(self, value):
        if self.rear is None:
            self.rear = 0
            print(self.rear)
            self.queData.append(value)
        elif self.rear < self.size:
            self.rear += 1
            self.queData.append(value)
        else:
            raise Exception("Max size reached")

    def deque(self):
        if self.front is None and self.rear is not None:
            self.front = 0
            del self.queData[self.front]
            self.rear -= 1
        elif self.rear is not None:
            self.front += 1
            del self.queData[self.front]
            self.rear -= 1
        elif self.rear < 0 or self.rear is None:
            raise Exception("Que is Empty")

    def printQue(self):
        print(*self.queData)


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
    t1.deque()
    t1.printQue()

### Time complexity
## enque -> O(1)
## deque -> O(1)
