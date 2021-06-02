class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        
        seen = set()
        
        def getArea(y, x):
            q = [(y, x)]
            size = 0
            
            seen.add((y,x))
            while len(q):
                y, x = q.pop()
                size += 1
                for c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= y + c[0] < N and 0 <= x + c[1] < M and (y + c[0], x+c[1]) not in seen and grid[y+c[0]][x+c[1]] == 1:
                        seen.add((y+c[0], x+c[1]))
                        q.append((y+c[0], x+c[1]))
                    
            return size
            
        best = 0
        for y in range(N):
            for x in range(M):
                if grid[y][x] == 1 and (y,x) not in seen:
                    best = max(best, getArea(y,x))
                
        return best
                    
                