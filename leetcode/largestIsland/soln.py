class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        
        islandID = 2
        islandSize = defaultdict(int)
        seen = set()
        
        def bfs(startNode, islandNum):
            nonlocal islandSize, seen
            q = [(startNode[0], startNode[1])]
            size = 1
            while q:
                
                y, x = q.pop()
                islandSize[islandNum] = max(islandSize[islandNum], size)
                grid[y][x] = islandNum
                for c in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    ny = c[0] + y
                    nx = c[1] + x
                    if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in seen and grid[ny][nx] == 1:
                        seen.add((ny,nx))
                        size += 1
                        
                        q.append((ny, nx))
                        
        for y in range(N):
            for x in range(M):
                if grid[y][x] == 1:
                    bfs((y,x), islandID)
                    islandID += 1
                    
        best = 0
        
        for y in range(N):
            for x in range(M):
                if grid[y][x] == 0:
                    cand = 1
                    candislands = set()
                    
                    if 0 <= y-1 < N:
                        if grid[y-1][x] > 0:
                            candislands.add(grid[y-1][x])
                    if 0 <= y+1 < N:
                        if grid[y+1][x] > 0:
                            candislands.add(grid[y+1][x])
        
                    if 0 <= x-1 < M:
                        if grid[y][x-1] > 0:
                            candislands.add(grid[y][x-1])
                    if 0 <= x+1 < M:
                        if grid[y][x+1] > 0:
                            candislands.add(grid[y][x+1])
                    
                    for group in candislands:
                        cand += islandSize[group]
                        
                    best = max(best, cand)
        
        for size in islandSize.values():
            best = max(best, size)
            
        #print(islandSize)
        return best
    