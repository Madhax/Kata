class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
       
        dp = [[0 for _ in range(n)] for _ in range(m)]
       
        for y in range(m):
            for x in range(n):
                ans = math.inf
                if y == 0 and x == 0:
                    ans = grid[y][x]
                if y > 0:
                    ans = min(ans, grid[y][x] + dp[y-1][x])
                if x > 0:
                    ans = min(ans, grid[y][x] + dp[y][x-1])
                   
               
                dp[y][x] = ans
                #dp[y][x] = grid[y][x] + min(dp[y-1][x], dp[y][x-1])
               
        print(dp)
        return dp[m-1][n-1]
   
        """
        def dp(y, x):
            nonlocal grid
           
            if y == m-1 and x == n-1:
                return grid[y][x]
           
            ans = math.inf
            if y < m-1:
                ans = min(ans, grid[y][x] + dp(y+1, x))
               
            if x < n-1:
                ans = min(ans, grid[y][x] + dp(y, x+1))
               
            return ans
       
        return dp(0,0)"""