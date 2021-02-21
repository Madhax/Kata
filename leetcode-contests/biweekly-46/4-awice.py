class Solution(object):
    def getCoprimes(self, A, edges):
        n = len(edges) + 1
        graph = [[] for _ in xrange(n)]
        for u,v  in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        from fractions import gcd
        ans = [-1] * n
        
        
        paths = [[] for p in range(51)]
        timer = {}
        def dfs(node, par=None, time=0):
            timer[node] = time
            v = A[node]
            best = None
            for i, row in enumerate(paths):
                if i and gcd(v, i) == 1 and row:
                    last = row[-1]
                    if best is None or timer[last] > timer[best]:
                        best = last
            if best is not None:
                ans[node] = best
            
            paths[v].append(node)
            for nei in graph[node]:
                if nei != par:
                    dfs(nei, node, time+1)
            paths[v].pop()
            
        dfs(0)
        return ans