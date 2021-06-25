from functools import lru_cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(i, j, u):
            #if u <= 0 or i < 0 or i >= m or j < 0 or j >= n:
            if (i < 0 or i >= m or j < 0 or j >= n):
                return 1
            elif u <=0:
                return 0
            return dfs(i-1, j, u-1) + dfs(i+1, j, u-1) + dfs(i, j-1, u-1) + dfs(i, j+1, u-1)
        
        return dfs(startRow, startColumn, maxMove) % (10**9+7)