class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        @functools.cache
        def dp(row, index):
            nonlocal triangle
            
            if row == len(triangle):
                return 0
            
            ret = math.inf
            ret = min(ret, triangle[row][index] + dp(row+1, index))
            ret = min(ret, triangle[row][index] + dp(row+1, index+1))
            
            return ret
        """
        
        dp = [math.inf for _ in range(len(triangle[-1]))]
        dp[0] = triangle[0][0]
        for y in range(1, len(triangle)):
            ndp = [math.inf for _ in range(len(triangle[-1]))]
            for x in range(y+1):
                #print(y, x)
                ndp[x] = min(ndp[x], triangle[y][x] + dp[x])
                ndp[x] = min(ndp[x], triangle[y][x] + dp[x-1] if x > 0 else math.inf)
            
            dp[:] = ndp
            #print(dp)
        return min(dp)