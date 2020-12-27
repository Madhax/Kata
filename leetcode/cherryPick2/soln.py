class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        dp = [[[0 for _ in range (70) ] for _ in range(70] for _ in range(70)]
        
        def fn(row, r1, r2):
            nonlocal dp, grid

            if r1 < 0 or r1 >= len(grid[0]) or r2 < 0 or r2 >= len(grid[0]):
                return 0

            if dp[row][r1][r2] != 0:
                return dp[row][r1][r2]
        
            res = grid[row][r1] + grid[row][r2]

            if r1 == r2:
                res -= grid[row][r1]

            if row < len(grid)-1:
                mxx = 0

                for j1 in range(r1 - 1, r1 + 2):
                    for j2 in range(r2 - 1, r2 + 2):
                        mxx = max(mxx, fn(row+1, j1, j2))

            res += mxx

            dp[row][r1][r2] = res
            return res
        
        
                
                    
        return fn(0,0, len(grid[0]) - 1)
    