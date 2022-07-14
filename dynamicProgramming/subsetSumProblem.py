"""
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
"""


class subset(object):

    def __init__(self, n, w):
        self.memoizeArray = [[-1 for i in range(w + 1)] for y in range(n + 1)]

    def recursiveApproach(self, data, n, w):
        if n < 0 or w < 0:
            return False
        elif n == 0 and w == 0:
            return True
        elif data[n - 1] <= w:
            return self.recursiveApproach(data, n - 1, w - data[n - 1]) or self.recursiveApproach(data, n - 1, w)
        else:
            return self.recursiveApproach(data, n - 1, w)

    def dpMemoize(self, data, n, w):
        if n < 0 or w < 0:
            return False
        elif n == 0 and w == 0:
            return True
        elif self.memoizeArray[n][w] != -1:
            return self.memoizeArray[n][w]
        elif data[n - 1] <= w:
            self.memoizeArray[n][w] = self.recursiveApproach(data, n - 1, w - data[n - 1]) or self.recursiveApproach(
                data, n - 1, w)
            return self.memoizeArray[n][w]
        else:
            self.memoizeArray[n][w] = self.recursiveApproach(data, n - 1, w)
            return self.memoizeArray[n][w]

    def dpTabulation(self, arr, n, w):
        memoizeArray = [[0 for i in range(w + 1)] for y in range(n + 1)]
        memoizeArray[0][0] = True

        ### This below is used for initializing the 1 row /column of
        ###tabulation matrix
        for i in range(1, w + 1):
            memoizeArray[0][i] = False
        for y in range(1, n + 1):
            memoizeArray[y][0] = True

        ### END of INITIALIZATION

        for i in range(1, n + 1):
            for y in range(1, w + 1):
                if arr[i - 1] <= y:
                    memoizeArray[i][y] = memoizeArray[i - 1][y - arr[i - 1]] or memoizeArray[i - 1][y]
                else:
                    memoizeArray[i][y] = memoizeArray[i - 1][y]
        return memoizeArray[n][w]


if __name__ == "__main__":
    #data = [2, 3, 7, 8, 11]
    data = [3, 34, 4, 12, 5, 2]
    n = len(data)
    w = 9
    t1 = subset(n, w)
    print(t1.recursiveApproach(data, n, w))
    # print(t1.dpMemoize(data, n, w)) -> Time Complexity -> O(nw) but additional stack space complexity
    # print(t1.dpTabulation(data, n, w)) -> Time Complexity -> O(nw) and space complexity O(mn)
