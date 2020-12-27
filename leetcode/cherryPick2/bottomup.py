class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        dp = [[0] * (m + 2) for _ in range(m + 2)]
        dp[0][m-1] = grid[0][0] + grid[0][m-1]

        for i in range(1, n): # each level
            tmp = [[0] * (m + 2) for _ in range(m + 2)]
            # each time, you can move one more to left or right, so the most one is i+1 or m-1-i
            for j in range(min(i + 1, m)): # robot 1'col,
                for k in range(max(m - i - 1, 0), m): # robot 2'col
                    if j != k:
                        tmp[j][k] = max(dp[j-1][k],   dp[j][k],   dp[j+1][k],
                                        dp[j-1][k-1], dp[j][k-1], dp[j+1][k-1],
                                        dp[j-1][k+1], dp[j][k+1], dp[j+1][k+1])
                        tmp[j][k] += grid[i][j] + grid[i][k]

            dp = tmp[:][:]

        return max(max(i) for i in dp)