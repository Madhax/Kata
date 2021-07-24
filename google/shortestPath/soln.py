class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M = len(grid[0])
        N = len(grid)
        
        def h(cury, curx, endy, endx):
            return math.sqrt((curx- endx)**2 + (cury-endy)**2)
        
        def bfs():
            
            q = collections.deque()
            
            #k is entry
            seen = set()
            seen.add((0,0,k))
            #heappush(q, (0, 0, 0, k))
            q.append((0,0,k))
            result = math.inf
            ans = 0
            if k>len(grid)-1+len(grid[0])-1:
                return len(grid)-1+len(grid[0])-1
            while q:
                for _ in range(len(q)):
                    
                    cury, curx, curk = q.popleft()

                    if cury == N-1 and curx == M-1:
                        return ans
                    for c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ny = cury + c[0]
                        nx = curx + c[1]

                        if 0 <= ny < N and 0 <= nx < M:
                            if grid[ny][nx] == 1 and curk > 0 and (ny,nx,curk-1) not in seen:
                                seen.add((ny,nx,curk-1))
                                q.append((ny, nx, curk-1))
                                    #heappush(q, (score+1, ny, nx, curk-1))
                            elif grid[ny][nx] == 0 and (ny,nx,curk) not in seen:
                                seen.add((ny,nx,curk))
                                q.append(( ny, nx, curk))
                                    #heappush(q, (score+1, ny, nx, curk))
                                
                ans += 1
            
            return -1
        
        return bfs()
    
    