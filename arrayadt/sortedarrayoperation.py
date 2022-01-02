from array import array


class SortedArrayOperation(object):

    def __init__(self):
        self.array = array('i', [4, 8, 13, 23, 26, 33])

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


if __name__ == "__main__":
    t1 = SortedArrayOperation()
    # print(t1.insertElement(34))
    print(t1.isSorted())
