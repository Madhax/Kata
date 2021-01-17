class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        a = matrix
        n, m = len(a), len(a[0])
        c = [0]*m
        r = 0
        for i in xrange(n):
            c = [c[j]+1 if a[i][j]==1 else 0 for j in xrange(m)]
            d = sorted(c, reverse=True)
            h = d[0]
            for j in xrange(m):
                h = min(h, d[j])
                if h == 0: break
                r = max(r, h*(j+1))
        return r