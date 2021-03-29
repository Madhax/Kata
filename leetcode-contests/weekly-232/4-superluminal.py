class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        par = [-1] * n
        rnk = [0] * n
        sz = [1] * n
        def _find(u):
            path = []
            while par[u] >= 0:
                path.append(u)
                u  = par[u]
            for v in path:
                par[v] = u
            return u
        def _union(u, v):
            u = _find(u)
            v = _find(v)
            if u == v: return
            if rnk[u] < rnk[v]:
                u, v = v, u
            par[v] = u
            sz[u] += sz[v]
            if rnk[u] == rnk[v]:
                rnk[u] += 1
        def _size(u):
            return sz[_find(u)]

        r = 0
        vis = [False] * n
        for u in sorted(range(n), key=lambda i: -nums[i]):
            vis[u] = True
            if u-1 >= 0 and vis[u-1]: _union(u, u-1)
            if u+1 < n and vis[u+1]: _union(u, u+1)
            if vis[k] and _find(u) == _find(k):
                r = max(r, _size(u) * nums[u])
        return r