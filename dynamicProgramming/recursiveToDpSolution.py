"""
https://www.geeksforgeeks.org/min-cost-path-dp-6/
Modified Problem
Min distance for reaching any point to any point
Solution for Easy DP problem
"""

import sys


class MinCostPath:

    def __init__(self, cost=None):
        self.dpMatrix = [[-1 for i in range(len(cost) + 1)] for y in range(len(cost) + 1)]
        pass

    def getMinPathRecursive(self, cost_matrix=None, t=0, p=0, m=0, n=0):
        if t > m or p > n:
            return sys.maxsize
        elif t == m and p == n:
            return cost_matrix[t][p]
        else:
            return (cost_matrix[t][p] + min(self.getMinPathRecursive(cost_matrix, t + 1, p + 1, m, n),
                                            self.getMinPathRecursive(cost_matrix, t, p + 1, m, n),
                                            self.getMinPathRecursive(cost_matrix, t + 1, p, m, n)))

    def getMinPathDpWithMemoize(self, cost_matrix=None, t=0, p=0, m=0, n=0):

        if t > m or p > n:
            return sys.maxsize
        elif t == m and p == n:
            return cost_matrix[t][p]
        elif self.dpMatrix[t][p] != -1:
            return self.dpMatrix[t][p]
        else:
            self.dpMatrix[t][p] = (
                    cost_matrix[t][p] + min(self.getMinPathDpWithMemoize(cost_matrix, t + 1, p + 1, m, n),
                                            self.getMinPathDpWithMemoize(cost_matrix, t, p + 1, m, n),
                                            self.getMinPathDpWithMemoize(cost_matrix, t + 1, p, m, n)))
            return self.dpMatrix[t][p]

    def getMinPathWithTabulation(self, cost=None, m=0, n=0):

        dpMatrix = [[0 for x in range(m + 1)] for x in range(n + 1)]

        dpMatrix[0][0] = cost[0][0]

        for i in range(1, m + 1):
            dpMatrix[i][0] = cost[i][0] + dpMatrix[i - 1][0]

        for j in range(1, n + 1):
            dpMatrix[0][j] = cost[0][j] + dpMatrix[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dpMatrix[i][j] = min(dpMatrix[i - 1][j - 1], dpMatrix[i - 1][j],
                                     dpMatrix[i][j - 1]) + cost[i][j]

        return dpMatrix[m][n]



if __name__ == "__main__":
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    t1 = MinCostPath(cost)
    # print(t1.getMinPathRecursive(cost_matrix=cost, t=0, p=0, m=1, n=2))
    print(t1.getMinPathDpWithMemoize(cost_matrix=cost, t=0, p=0, m=2, n=2))
    print(t1.getMinPathWithTabulation(cost, m=2, n=2))
