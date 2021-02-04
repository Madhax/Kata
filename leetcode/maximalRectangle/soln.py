class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        
        if m == 0:
            return 0
        
        n = len(matrix[0])
        
        @functools.cache
        def getMaxHorizontal(y, x):
            nonlocal matrix, n
            
            if x >= n:
                return 0
            
            if matrix[y][x] == "0":
                return 0
            
            return 1 + getMaxHorizontal(y, x+1)
        
        
        #print(getMaxHorizontal(0,0))
        best = 0
        for y in range(m):
            for x in range(n):
                curWidth = math.inf
                for z in range(y, m):
                    if matrix[z][x] == 0:
                        break
                        
                    curWidth = min(curWidth, getMaxHorizontal(z, x))
                    
                    if curWidth == 0:
                        break
                        
                    if best / curWidth > m - y:
                        #print(best, curWidth, m, z)
                        break
                        
                    curArea = (z-y+1) * curWidth
                    
                    if curArea > best:
                        #print(curWidth, z, x)
                        best = curArea
        
        return best
            
            