from sortedcontainers import SortedList
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        N = len(matrix)
        M = len(matrix[0])
        q = []
        
        nmatrix = [[-math.inf for _ in range(M)] for _ in range(N)]
        for y in range(N):
            for x in range(M):
                heapq.heappush(q, (matrix[y][x], y,x))
                
                
        memocol = defaultdict(SortedList)
        memorow = defaultdict(SortedList)
        
        s = set()
        def normalize(val, y, x):
            if (y,x) in s:
                return
            s.add((y,x))
            nmatrix[y][x] = val
            if y in memorow:
                score, ny, nx = memorow[y][-1]
                
                if matrix[y][x] == matrix[ny][nx]:
                    normalize(val, ny, nx)
                    
            if x in memocol:
                score, ny, nx = memocol[x][-1]
                
                if matrix[y][x] == matrix[ny][nx]:
                    normalize(val, ny, nx)
        
            s.remove((y,x))
            
        while q:
            _, y, x = heappop(q)
            #print(y,x)
            highestAdj = -math.inf
            val = 1
            hasEqual = False
            hasEqualChanged = False
            if y in memorow:
                score, ny, nx = memorow[y][-1]
                
                if matrix[y][x] == matrix[ny][nx]:
                    val = max(val, nmatrix[ny][nx])
                    hasEqual = True
                else:
                    val = max(val, nmatrix[ny][nx]+1)
                    
            if x in memocol:
                score, ny, nx = memocol[x][-1]
                
                if matrix[y][x] == matrix[ny][nx]:
                    val = max(val, nmatrix[ny][nx])
                    hasEqual = True
                else:
                    val = max(val, nmatrix[ny][nx]+1)
                    
            
            if hasEqual:
                normalize(val, y, x)
                
            
            nmatrix[y][x] = val
            memorow[y].add((val, y, x))
            memocol[x].add((val, y, x))
                    
                
            """
            for delta in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ny = y + delta[0]
                nx = x + delta[1]
                
                
                if 0 <= ny < N and 0 <= nx < M:
                    if nmatrix[ny][nx] > -math.inf:
                        if matrix[ny][nx] == matrix[y][x]:
                            val = max(val, nmatrix[ny][nx])
                            
                        else:
                            
                            val = max(val, nmatrix[ny][nx]+1)
                            print("!", val)
            """
            
            
            
            #print(val)
            nmatrix[y][x] = val
                
            
        return nmatrix
            
            