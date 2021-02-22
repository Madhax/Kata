class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
        DP word1+word2
        get max from ranges starting in both strings to guarantee non-empty

        """ 
        n1, n2 = len(word1), len(word2)
        s = word1 + word2
        n = len(s)
        f = [[0]*n for _ in xrange(n)]
        for i in xrange(n): f[i][i] = 1
        for l in xrange(2, 1+n):
            for i in xrange(1+n-l):
                j = i + l - 1
                f[i][j] = max(f[i][j-1], f[i+1][j])
                if s[i] == s[j]:
                    f[i][j] = max(f[i][j], 2 + f[i+1][j-1])
        best = 0
        for i in xrange(n1):
            for j in xrange(n1, n):
                if s[i] == s[j]:
                    best = max(best, 2 + f[i+1][j-1])
        return best
