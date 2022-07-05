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



if __name__ == "__main__":
    listData = [3, 6, 8, 12, 14, 17, 25, 29.31, 36, 42, 47, 53, 55, 62]
    t1 = BinarySearch(listData)
    print(t1.searchElementPosition(-1))
