class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1: return sum(min(1, x) for x in nums)
        c = [Counter() for _ in xrange(k)]
        for i, v in enumerate(nums): c[i%k][v] += 1
        m = 1 << max(nums).bit_length()
        f = [float('-inf')] * m
        f[0] = 0
        for i in xrange(k):
            ff = f[:]
            for x in xrange(m):
                for y, v in c[i].iteritems():
                    ff[x^y] = max(ff[x^y], f[x]+v)
            lb = max(f)
            for i in xrange(m):
                f[i] = max(ff[i], lb)
        return len(nums) - f[0]