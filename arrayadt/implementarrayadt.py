import array


class ArrayADT:

    def __init__(self):
        self.array = array.array("i", [2, 3, 6, 9, 8])
        pass

    def insertelement(self, index: int, value: int):
        currentlength = len(self.array)
        self.array.append(1)

        if index <= currentlength:
            for i in range(currentlength, index - 1, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = value
        else:
            raise IndexError

    def deleteelement(self, index: int):
        currentlength = len(self.array)
        if index <= currentlength:
            for i in range(index, currentlength - 1):
                self.array[i] = self.array[i + 1]
            self.array.pop()
        else:
            raise IndexError


if __name__ == "__main__":
    t1 = ArrayADT()
    print(t1.array)
    t1.insertelement(2, 7)
    print(t1.array)
    t1.deleteelement(3)
    print(t1.array)
