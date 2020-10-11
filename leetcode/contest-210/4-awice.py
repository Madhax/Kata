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
    def countSubgraphsForEachDiameter(self, N, edges):
        graph = [[] for _ in xrange(N)]
        
        for i,(u,v)  in enumerate(edges):
            u-=1
            v-=1
            graph[u].append(v)
            graph[v].append(u)
            edges[i] = [u,v]
        #dsu = DSU()
        def bfs(source, mask):
            queue = [[source, None, 0]]
            
            for node, par, d in queue:
                for nei in graph[node]:
                    if nei != par and mask[nei] == '1':
                        queue.append([nei, node, d + 1])
            return node, d

        ans = [0] * N
        for mask in xrange(1, 1 << N):
            bmask = bin(mask)[2:][::-1]
            if len(bmask) < N:
                bmask = bmask + '0' * (N - len(bmask))
            popcount = bmask.count('1')
            root = bmask.index('1')
            ecount = 0
            for u,v  in edges:
                if bmask[u]==bmask[v]=='1':
                    ecount += 1
            if ecount + 1 == popcount:
                # find max distance
                # print("mask", bmask, mask)
                v1, d1 = bfs(root, bmask)
                v2, d2 = bfs(v1, bmask)
                ans[d2] += 1
                
        # print('a', ans)
        ans.pop(0)
        return ans