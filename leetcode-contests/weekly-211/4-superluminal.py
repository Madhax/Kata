class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        par = [-1] * (n+1)
        rank = [0] * (n+1)
        def _find(u):
            path = []
            while par[u] != -1:
                path.append(u)
                u = par[u]
            for v in path:
                par[v] = u
            return u
        def _union(u, v):
            u = _find(u)
            v = _find(v)
            if u == v: return False
            if rank[u] > rank[v]:
                u, v = v, u
            par[u] = v
            if rank[u] == rank[v]:
                rank[v] += 1
            return True
        for d in xrange(threshold+1, n+1):
            for i in xrange(2*d, n+1, d):
                _union(d, i)
        return [_find(u)==_find(v) for u, v in queries]
