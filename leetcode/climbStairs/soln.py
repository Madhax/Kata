class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
       
        if n == 2:
            return 2
       
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
       
        for x in range(2, n):
            dp[x] = dp[x-1]+dp[x-2]
           
        return dp[n-1]
   
        """
        @functools.cache
        def dp(step):
            nonlocal n
            if n == step:
                return 1
           
            ans = 0
            if step < n:
                ans += dp(step+1)
               
            if step < n-1:
                ans += dp(step+2)
           
            return ans
       
        return dp(0)"""