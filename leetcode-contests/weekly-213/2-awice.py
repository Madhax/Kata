class Solution(object):
    def countVowelStrings(self, n):
        dp = [1] * 5
        for i in xrange(n - 1):
            ndp = [0] * 5
            for j in xrange(5):
                for j0 in xrange(j + 1):
                    ndp[j] += dp[j0]
            dp = ndp
        
        return sum(dp)