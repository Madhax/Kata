class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recursions
        
        
        #let dp(y,x) be number of paths to y,x
        
        @functools.cache
        def dp(y,x):
            nonlocal m, n
            
            if y == m-1 and x == n-1:
                return 1
            
            ans = 0
            
            if x < n-1:
                ans += dp(y, x+1)
                
            if y < m-1:
                ans += dp(y+1, x)
                
            return ans
        
        return dp(0,0)
            
            