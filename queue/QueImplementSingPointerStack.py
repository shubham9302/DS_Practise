class QueData:
    def __init__(self, size=None):
        self.queData = []
        self.size = size
        self.rear = None

    def enque(self, value):
        if self.rear is None:
            self.rear = 0
            print(self.rear)
            self.queData.append(value)
        elif self.rear < self.size-1:
            self.rear += 1
            self.queData.append(value)
        else:
            raise Exception("Max size reached")

    def deque(self):
        for element in range(0, self.rear):
            self.queData[element] = self.queData[element + 1]
        del self.queData[-1]
        self.rear -= 1

    def printQue(self):
        print(*self.queData)


if __name__ == "__main__":
    t1 = QueData(5)
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
## deque -> O(n)