class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        N = len(maze)
        M = len(maze[0])
        
        def bfs(entrance):
            
            q = deque([(entrance[0], entrance[1], 0)])
            seen = set()
            seen.add((entrance[0], entrance[1]))
            while q:
                
                y, x, steps = q.popleft()
                
                
                if (y in [0, N-1] or x in [0, M-1]) and steps > 0:
                    return steps
                
                for c in [[0,1], [0,-1], [1,0], [-1,0]]:
                    ny = y + c[0]
                    nx = x + c[1]
                    
                    if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == ".":
                        if (ny,nx) not in seen:
                            seen.add((ny,nx))
                            q.append((ny,nx,steps+1))
                            
                    
                
            return -1
            
            
        return bfs(entrance)
