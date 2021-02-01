class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        a = matrix
        n, m = len(a), len(a[0])
        s = [[0]*(m+1) for _ in xrange(n+1)]
        b = []
        for i in xrange(n):
            for j in xrange(m):
                s[i+1][j+1] = a[i][j] ^ s[i][j] ^ s[i+1][j] ^ s[i][j+1]
                b.append(s[i+1][j+1])
        b.sort(reverse=True)
        return b[k-1]