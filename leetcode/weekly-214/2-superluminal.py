class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = float('inf')
        r = 0
        for i in sorted(Counter(s).itervalues(), reverse=True):
            if p <= 1:
                r += i
            elif i >= p:
                r += i - (p-1)
                p -= 1
            else:
                p = i
        return r