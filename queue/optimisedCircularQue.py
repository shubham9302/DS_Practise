class QueData:
    def __init__(self, size=None):
        self.queData = [None] * size
        self.size = size
        self.rear = 0
        self.front = 0

    def enque(self, value):
        if (self.rear + 1) % self.size == self.front:
            return "Que is full"
        else:
            self.rear = (self.rear + 1) % self.size
            self.queData[self.rear] = value

    def deque(self):
        if self.rear == self.front:
            return "Que is empty"
        else:
            self.front = (self.front + 1) % self.size
            value = self.queData[self.front]
            return value

    def printQue(self):
        print(*self.queData)


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
