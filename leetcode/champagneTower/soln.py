import functools
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        @lru_cache
        def getPour(i,j):
            if i < 0:
                return poured
            
            if j > i or j < 0:
                return 0
            
            #minus 1 for current cup
            return max(0, 0.5*getPour(i-1, j-1) + 0.5*getPour(i-1,j) - 1)
        
        return min(1, 0.5*getPour(query_row-1, query_glass-1) + 0.5*getPour(query_row-1, query_glass))
    
    