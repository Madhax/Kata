class DSU(object):

    def __init__(self, n):
        self.rank = [0 for x in range(n)]
        self.parents = [x for x in range(n)]

    def findRoot(self, x):

        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]

        return x

    def union(self, i, j):

        rootI = self.findRoot(i)
        rootJ = self.findRoot(j)

        if rootI == rootJ:
            return False

        if self.rank[rootI] < self.rank[rootJ]:
            self.parents[rootI] = rootJ

        elif self.rank[rootI] == self.rank[rootJ]:
            self.parents[rootI] = rootJ
            self.rank[rootJ] += 1

        else:
            self.parents[rootJ] = root I

        return True


class Solution(object):
    def findRedundantConnection(self, edges):

        dsu = DSU(len(edges))
        for i, j in edges:
            if not dsu.union(i-1, j-1):
                return [i,j]

        return []
        