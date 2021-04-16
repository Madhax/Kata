class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = 0
        dp[1] = 1
        for x in range(2, n+1):
            dp[x] = dp[x-1]+dp[x-2]
        
        return dp[n]