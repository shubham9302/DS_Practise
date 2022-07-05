from sorting.commonutil import Utilities


class selectionSort:

    def __init__(self, a):
        self.a = a

    def sort(self):
        n = len(self.a)
        for i in range(0, n):
            temp = i
            for y in range(i, n - 1):
                if self.a[temp] > self.a[y + 1]:
                    temp = y + 1
                    print("temp", temp)
            self.a = Utilities.swap(temp, i, self.a)
            print("self.a", self.a)
        return self.a


if __name__ == "__main__":
    arr = [8, 7, 5, 2, 3]
    t1 = selectionSort(arr)
    print(t1.sort())
