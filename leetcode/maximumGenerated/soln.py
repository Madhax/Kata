from functools import lru_cache
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
       
        @lru_cache(maxsize=None)
        def getVal(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n % 2 == 0:
                return getVal(n/2)
            else:
                return getVal((n-1)/2) + getVal((n-1)/2 + 1)
           
        return max(getVal(x) for x in range(n+1))