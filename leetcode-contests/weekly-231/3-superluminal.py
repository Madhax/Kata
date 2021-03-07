from heapq import heappush, heappop
class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in xrange(n)]
        for u, v, w in edges:
            adj[u-1].append((v-1, w))
            adj[v-1].append((u-1, w))

        h = []
        d = [float('inf')] * n
        def _consider(u, du):
            if d[u] <= du: return
            d[u] = du
            heappush(h, (du, u))
        _consider(n-1, 0)
        while h:
            du, u = heappop(h)
            for v, w in adj[u]: _consider(v, du + w)

        mod = 10**9 + 7
        ways = [0] * n
        ways[n-1] = 1
        for u in sorted(xrange(n), key=lambda i: d[i]):
            for v, _ in adj[u]:
                if d[v] < d[u]: ways[u] += ways[v]
            ways[u] %= mod
        return ways[0]
