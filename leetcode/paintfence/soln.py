class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        @functools.cache
        
        def dp(n):
            if n == 1:
                return k
            
            if n == 2:
                return k * k
            
            return (k-1) * (dp(n-1) + dp(n-2))
        
        return dp(n)