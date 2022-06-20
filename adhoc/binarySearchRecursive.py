class BinarySearch:

    def __init__(self, a):
        self.a = a

    def searchElementPosition(self, h, l, val):
        mid = int((l + h) / 2)
        if self.a[mid] == val:
            return mid
        elif h < l:
            return None
        else:
            if self.a[mid] > val:
                h = mid - 1
            else:
                l = mid + 1
            return self.searchElementPosition(h, l, val)


if __name__ == "__main__":
    listData = [3, 6, 8, 12, 14, 17, 25, 29.31, 36, 42, 47, 53, 55, 62]

    t1 = BinarySearch(listData)
    l = 0
    h = len(listData)
    print(t1.searchElementPosition(h, l, 62))
