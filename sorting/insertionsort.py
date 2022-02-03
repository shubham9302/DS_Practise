from sorting.commonutil import Utilities


class InsertionSort:

    def __init__(self, a):
        self.a = a

    def sort(self):
        n = len(self.a)
        for i in range(1, n):
            for y in range(0, i):
                if self.a[i] < self.a[y]:
                    self.a = Utilities.swap(i, y, self.a)
        return self.a


if __name__ == "__main__":
    arr = [8, 5, 7, 3, 2]
    t1 = InsertionSort(arr)
    print(t1.sort())
