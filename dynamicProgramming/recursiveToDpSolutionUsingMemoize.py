"""
https://www.geeksforgeeks.org/min-cost-path-dp-6/
Modified Problem
Min distance for reaching any point to any point
Solution for Easy DP problem
"""

import sys


class MinCostPath:

    def __init__(self,cost=None):
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

    def getMinPathDp(self, cost_matrix=None, t=0, p=0, m=0, n=0):

        if t > m or p > n:
            return sys.maxsize
        elif t == m and p == n:
            return cost_matrix[t][p]
        elif self.dpMatrix[t][p] != -1:
            return self.dpMatrix[t][p]
        else:
            self.dpMatrix[t][p] = (cost_matrix[t][p] + min(self.getMinPathDp(cost_matrix, t + 1, p + 1, m, n),
                                                           self.getMinPathDp(cost_matrix, t, p + 1, m, n),
                                                           self.getMinPathDp(cost_matrix, t + 1, p, m, n)))
            return self.dpMatrix[t][p]


if __name__ == "__main__":
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    t1 = MinCostPath(cost)
    print(t1.getMinPathRecursive(cost_matrix=cost, t=0, p=0, m=1, n=2))
    print(t1.getMinPathDp(cost_matrix=cost, t=0, p=0, m=2, n=2))
