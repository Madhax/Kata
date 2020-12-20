class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        dp = [[[0 for _ in range (len(grid[0])+3) ] for _ in range(len(grid)+3)] for _ in range(2)]
        
        def fn(row, r1, r2):
            nonlocal dp, grid

            if dp[row][r1][r2] != 0:
                return dp[row][r1][r2]
        
            res = grid[row][r1] + grid[row][r2]

            if col1 == col2:
                res -= grid[row][col1]

            if row < len(grid):
                mxx = 0

                for j1 in range(r1 - 1, r1 + 2):
                    for j2 in range(r2 - 1, r2 + 2):
                        mxx = max(mxx, fn(row+1, j1, j2))

            res += mxx

            dp[row][r1][r2] = res
            return res
        
        
                
                    
        return fn(0,0, len(grid[0]) - 1)
    