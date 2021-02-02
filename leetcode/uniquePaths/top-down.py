class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 or n == 1:
            return 1
        
        dp = [[0 for x in range(n)] for y in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
            
        for j in range(n):
            dp[0][j] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]
        
        
        # return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        #shantanu is gandu
        