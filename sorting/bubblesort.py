from sorting.commonutil import Utilities


class BubbleSort:

    def __init__(self, a):
        self.a = a

    def sort(self):
        array_length = len(self.a)
        for i in range(0, array_length):
            for y in range(0, array_length - i - 1):
                if self.a[y] > self.a[y + 1]:
                    self.a = Utilities.swap(y, y + 1, self.a)
        return self.a


if __name__ == "__main__":
    arr = [8, 5, 7, 3, 2]
    t1 = BubbleSort(arr)
    print(t1.sort())
