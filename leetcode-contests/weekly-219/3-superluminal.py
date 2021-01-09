
class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        a = stones
        n = len(a)

        s = [0] + a
        for i in xrange(n):
            s[i+1] += s[i]

        f = [0] * n
        for k in xrange(2, 1+n):
            f = [max(s[i+k]-s[i+1]-f[i+1], s[i+k-1]-s[i]-f[i])
                 for i in xrange(1+n-k)]
        return f[0]