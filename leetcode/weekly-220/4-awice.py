class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]
    
class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        edgeList.sort(key=lambda z: z[2])
        for i, query in enumerate(queries):
            query.append(i)
        
        queries.sort(key=lambda q: q[2])
        ans = [False] * len(queries)
        i = 0
        dsu = DSU(n)
        for p,q,limit,qid in queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                # print("!", edgeList[i], p,q,limit,qid)
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1
            
            if dsu.find(p) == dsu.find(q):
                ans[qid] = True
        return ans
            