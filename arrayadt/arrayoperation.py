import array
from arrayadt.implementarrayadt import ArrayADT


class ArrayOperation(ArrayADT):

    def __init__(self):
        super().__init__()
        print(self.array)

    def reversearraywithauxilayarray(self):
        """
        This function reverses the array using
        an additional array
        :return:
        """
        temparray = array.array('i')
        for i in range(len(self.array) - 1, -1, -1):
            temparray.append(self.array[i])

        for j in range(len(temparray)):
            self.array[j] = temparray[j]

    def reversearraywithswap(self):
        """
        This function reverses the array
        by swapping numbers
        :return:
        """

        for i in range(len(self.array)):
            j = (len(self.array) - 1) - i
            if i == j or i > j:
                break
            self.array[i], self.array[j] = self.array[j], self.array[i]

    def arraywithleftreverse(self):
        for i in range(0, len(self.array) - 1):
            j = i + 1
            self.array[i] = self.array[j]

        self.array[-1] = 1

    def arraywithleftrotate(self):
        for i in range(0, len(self.array) - 1):
            j = i + 1
            if i == 0:
                tempval = self.array[i]
            self.array[i] = self.array[j]

        self.array[-1] = tempval


if __name__ == "__main__":
    t1 = ArrayOperation()
    # t1.reversearraywithauxilayarray()
    # t1.reversearraywithswap()
    t1.arraywithleftreverse()
    print(t1.array)
