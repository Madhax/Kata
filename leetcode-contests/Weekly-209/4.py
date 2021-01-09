class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # this is simply inverse gray code
        a, b = n, 1
        while a:
            a = n >> b
            b <<= 1
            n ^= a
        return n
