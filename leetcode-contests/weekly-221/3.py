from functools import lru_cache
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        answer = []
        
        @lru_cache(maxsize=None)
        def passthrough(y, x):
            nonlocal grid
            if x < 0 or x >= len(grid[0]):
                -1
                
            if y >= len(grid):
                return x
            
            if x >= len(grid[0]) - 1 and grid[y][x] == 1:
                return -1
            
            if x == 0 and grid[y][x] == -1:
                return -1
            
            if grid[y][x] != grid[y][x+grid[y][x]]:
                return -1
            
            return passthrough(y+1, x + (grid[y][x]))
            
        
        
        for n in range(len(grid[0])):
            
            x = n
            y = 0
            
            answer.append(passthrough(0, x))

        return answer
                