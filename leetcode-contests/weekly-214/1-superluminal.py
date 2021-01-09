class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        n += 1
        arr = [0]*n
        arr[1] = 1
        for i in xrange(2, n):
            arr[i] = arr[i>>1]
            if i&1: arr[i] += arr[(i+1)>>1]
        return max(arr)