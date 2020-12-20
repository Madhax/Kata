from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Edge case not needed: if not grid or not grid[0]: return 0
        # Finish 1st Time REVIEW
        num_rows, num_cols = len(grid), len(grid[0])
        
        @lru_cache(None)
        def helper(row, col1, col2):
            if not (0<=col1<num_cols and 0<=col2<num_cols): return 0
            
            result = grid[row][col1] + (grid[row][col2] if col1!=col2 else 0)
            if row < (num_rows - 1):
                result += max(helper(row+1, col1+a, col2+b)
                             for a in [-1,0,1] for b in [-1,0,1])
            return result
        
        return helper(0, 0, num_cols-1)
        