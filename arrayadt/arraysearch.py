import array
from arrayadt.implementarrayadt import ArrayADT


class ArraySearch(ArrayADT):

    def __init__(self):
        super().__init__()
        self.data = array.array('i', [2, 3, 6, 8, 9, 12, 14])

    def linearsearch(self, element: int):
        c = None
        for i in range(len(self.array)):
            if self.array[i] == element:
                c = i
        return c

    def binarysearchrecursion(self, element, low, high):

        mid = int((low + high) / 2)
        if self.data[mid] != element:
            if self.data[mid] >= element:
                high = mid - 1
                return self.binarysearchrecursion(element, low, high)
            else:
                low = mid + 1
                return self.binarysearchrecursion(element, low, high)
        else:
            return mid

    def binarysearchloop(self, element, low=0, high=0):

        for i in range(0, len(self.data)):
            mid = int((low + high) / 2)
            if self.data[mid] == element:
                return mid
            elif self.data[mid] > element:
                high = mid - 1
            elif self.data[mid] < element:
                low = mid + 1


if __name__ == "__main__":
    t1 = ArraySearch()
    t1.insertelement(2, 7)
    print(t1.array)
    t1.deleteelement(3)
    print(t1.array)
    print(t1.linearsearch(-1))
    print(t1.binarysearchloop(9, 0, 6))
    print(t1.binarysearchrecursion(14, 0, 6))

