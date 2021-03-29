class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        maxSum -= n
        def f(h, w):
            w = min(w, h)
            return ((2*h+1-w)*w) // 2
        def test(val):
            return f(val, index+1) + f(val, n-index) - val <= maxSum
        a, b = 0, 1
        while test(b):
            b <<= 1
        while a + 1 < b:
            c = (a + b) >> 1
            if test(c): a = c
            else: b = c
        return b