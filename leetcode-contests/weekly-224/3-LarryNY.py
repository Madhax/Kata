class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        rmatrix = [[0] * rows for _ in range(cols)]
        for x in range(rows):
            for y in range(cols):
                rmatrix[y][x] = matrix[x][y]
                
        rmatrix.sort()
        for x in range(cols):
            for y in range(1, rows):
                if rmatrix[x][y] > 0:
                    rmatrix[x][y] = rmatrix[x][y-1] + 1
        #print(rmatrix)
        area = 0
        for x in range(rows):
            counts = collections.Counter()
            
            for y in range(cols):
                counts[rmatrix[y][x]] += 1
                
            current = 0
            for y in sorted(counts.keys(), reverse=True):
                current += counts[y]
                area = max(area, current * y)
            #print(counts)
        
        return area
        
