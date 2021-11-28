class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        N = len(land)
        M = len(land[0])
        
        farmID = 2
        seen = set()
        
        output = []
        
        def bfs(startNode, farmID):
            nonlocal seen, output
            q = [(startNode[0], startNode[1])]
            bottomRight = startNode
            size = 1
            while q:
                y, x = q.pop()
                if y >= bottomRight[0] and x >= bottomRight[1]:
                    bottomRight = (y,x)
                
                land[y][x] = farmID
                for c in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    ny = c[0] + y
                    nx = c[1] + x
                    if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in seen and land[ny][nx] == 1:
                        seen.add((ny,nx))
                        size += 1
                        q.append((ny, nx))
                        
            output.append([startNode[0], startNode[1], bottomRight[0], bottomRight[1]])
            
        for y in range(N):
            for x in range(M):
                if land[y][x] == 1:
                    bfs((y,x), farmID)
                    farmID += 1
                    
        return output
                    
        
