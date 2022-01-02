from array import array


class SortedArrayOperation(object):

    def __init__(self):
        # self.array = array('i', [4, 8, 13, 23, 26, 33])
        self.array = array('i', [-6, 3, -8, 10, 5, -7, -9, 12, 4, 2])

    def insertElement(self, element):
        appendCounter = 0
        for i in range(len(self.array) - 1, -1, -1):
            if self.array[i] > element:
                if appendCounter == 0:
                    self.array.append(element)
                    appendCounter += 1
                self.array[i + 1], self.array[i] = self.array[i], self.array[i + 1]
            else:
                if appendCounter == 0:
                    self.array.append(element)
                break
        return self.array

    def isSorted(self):
        for i in range(0, len(self.array) - 1):
            if self.array[i] > self.array[i + 1]:
                value = False
                break
            else:
                value = True
        return value

    def NegativeOnRight(self):
        j = len(self.array) - 1
        i = 0
        for i in range(0, len(self.array)):

            if self.array[i] < 0 and i < j:
                for y in range(j, 0, -1):
                    if self.array[y] >= 0:
                        self.array[y], self.array[i] = self.array[i], self.array[y]
                        j = j - 1
                        break
            elif i > j:
                break
        return self.array

    def NegativeOnRightOptimizedApproach(self):
        j = len(self.array) - 1
        i = 0
        while i < j:
            while self.array[i] >= 0:
                i = i + 1
            while self.array[j] < 0:
                j = j - 1
            if i < j:
                self.array[i], self.array[j] = self.array[j], self.array[i]

        return self.array

    def NegativeOnLeft(self):
        j = len(self.array) - 1
        i = 0
        while i < j:
            while self.array[i] < 0:
                i = i + 1
            while self.array[j] >= 0:
                j = j - 1
            if i < j:
                self.array[i], self.array[j] = self.array[j], self.array[i]

        return self.array


if __name__ == "__main__":
    t1 = SortedArrayOperation()
    # print(t1.insertElement(34))
    # print(t1.isSorted())
    print(t1.NegativeOnRight())
    print(t1.NegativeOnLeft())
    print(t1.NegativeOnRightOptimizedApproach())
