""""
We should write mid as (low + ((high -low)/2)))
This repersentation helps in reducing overflow
condition
if we write mid = (low + high) /2
and if the array size if very big low + high
can result in overflow

"""


class BinarySearch:

    def __init__(self, a):
        self.a = a

    def searchElementPosition(self, val):
        l = 0
        h = len(self.a) - 1
        state = False
        position = "Not Found"
        while not state and h >= l:
            mid = int((l + h) / 2)
            if self.a[mid] == val:
                state = True
                position = mid
            elif self.a[mid] > val:
                h = mid - 1
            else:
                l = mid + 1
        return position

    def searchElementPositionReverse(self, a, val):
        l = 0
        h = len(a) - 1
        state = False
        position = "Not Found"
        while not state and h >= l:
            mid = int((l + h) / 2)
            if a[mid] == val:
                state = True
                position = mid
            elif a[mid] > val:
                l = mid + 1
            else:
                h = mid - 1
        return position

    def firstOcurrence(self, a, val):
        l = 0
        h = len(a) - 1
        res = -1
        while h >= l:
            mid = int((l + h) / 2)
            if self.a[mid] == val:
                res = mid
                h = mid - 1
            elif self.a[mid] > val:
                h = mid - 1
            else:
                l = mid + 1
        return res

    def lastOcurrence(self, a, val):
        l = 0
        h = len(a) - 1
        res = -1
        while h >= l:
            mid = int((l + h) / 2)
            if self.a[mid] == val:
                res = mid
                l = mid + 1
            elif self.a[mid] > val:
                h = mid - 1
            else:
                l = mid + 1
        return res


if __name__ == "__main__":
    listData = [3, 6, 8, 12, 14, 17, 25, 29.31, 36, 42, 47, 53, 55, 62]
    reversedData = [listData[i] for i in range(len(listData) - 1, -1, -1)]
    t1 = BinarySearch(listData)
    print(t1.searchElementPosition(-1))
    print(t1.searchElementPositionReverse(reversedData, 6))
