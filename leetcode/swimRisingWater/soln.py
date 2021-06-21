class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        seen = set()
        
        def bfs():    
            q = [(grid[0][0],0,0)]
            seen.add((0,0))
            currentMax = grid[0][0]
            while len(q) > 0:
                depth, y, x = heapq.heappop(q)
                
                currentMax = max(currentMax, depth)
                
                if y == N-1 and x == M-1:
                    return currentMax
                
                for c in [[1,0],[-1,0],[0,1],[0,-1]]:
                    ny = y + c[0]
                    nx = x + c[1]
                    if 0 <= ny < N and 0 <= nx < M and (ny,nx) not in seen:
                        seen.add((ny,nx))
                        heapq.heappush(q, (grid[ny][nx], ny, nx))
                
            return currentMax
        
        return bfs()
    
    