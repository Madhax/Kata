class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        
        def bfs():
            q = deque()
            q.append((0, 0, 0))
            
            seen = set()
            
            while len(q) > 0:
                
                curx, cury, steps = q.popleft()
                #print(curx, cury, steps)
                
                for dx, dy in [[-2, -1], [-2, 1], [-1, 2], [-1, -2], [2, 1], [2, -1], [1, -2], [1, 2]]:
                    nx = curx + dx
                    ny = cury + dy
                    
                    if (nx, ny) in seen:
                        continue
                        
                    seen.add((nx, ny))
                    if (nx == x and ny == y):
                        return steps + 1
                    
                    q.append((nx, ny, steps+1))
                    
        return bfs()