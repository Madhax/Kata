class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        @functools.cache
        def left(y,x):
            if x == -1:
                return
            
            matrix[y][x] = 0
            left(y, x-1)
                  
        @functools.cache
        def up(y,x):
            if y == -1:
                return
            matrix[y][x] = 0
            up(y-1, x)
     
        rowset = set()
        colset = set()
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    left(y,x)
                    up(y,x)
                    rowset.add(y)
                    colset.add(x)
                elif y in rowset:
                    matrix[y][x] = 0
                elif x in colset:
                    matrix[y][x] = 0
                    
        return matrix
                    