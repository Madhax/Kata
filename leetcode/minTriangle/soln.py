class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle[-1]) 
        """
        dp = [[math.inf] * N for _ in range(N)]
        dp[0][0] = triangle[0][0]
        for y in range(1, N):
            for x in range(0, y+1):
                dp[y][x] = min(dp[y-1][x]+triangle[y][x], dp[y-1][x-1]+triangle[y][x] if x > 0 else math.inf)
        #print(dp)
        return min(dp[N-1])
        """
        
        dp = [math.inf] * N
        dp[0] = triangle[0][0]
        dp2 = [math.inf] * N
        dp2[0] = triangle[0][0]
        for y in range(1, N):
            for x in range(0, y+1):
                if y % 2 == 0:
                    tmp1 = dp2[x]+triangle[y][x]
                    tmp2 = dp2[x-1]+triangle[y][x] if x > 0 else math.inf
                    dp[x] = min(tmp1, tmp2)
                else:
                    tmp1 = dp[x]+triangle[y][x]
                    tmp2 = dp[x-1]+triangle[y][x] if x > 0 else math.inf
                    dp2[x] = min(tmp1, tmp2)
                
        if N % 2 == 0:
            return min(dp2)
        else:
            return min(dp)