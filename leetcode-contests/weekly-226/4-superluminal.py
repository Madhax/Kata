class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        ispalin = [[False]*(n+1) for _ in xrange(n+1)]
        for i in xrange(n):
            for k in xrange(n):
                if i-k<0 or i+k>=n or s[i-k]!=s[i+k]: break
                ispalin[i-k][i+k+1] = True
            if i == n-1 or s[i] != s[i+1]: continue
            for k in xrange(n):
                if i-k<0 or i+1+k>=n or s[i-k]!=s[i+1+k]: break
                ispalin[i-k][i+k+2] = True
                continue
        return any(ispalin[0][i] and ispalin[i][j] and ispalin[j][n]
                   for i in xrange(1, n)
                   for j in xrange(i+1, n))