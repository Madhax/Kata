class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
                      
        level = 0
        found = True
        
        rows = len(mat)
        cols = len(mat[0])
        
        while found:
            
            found = False
            level += 1
            for row in range(0, rows):
                for col in range(0, cols):
                    
                    if mat[row][col] == level:
                        if not (col < cols - 1 and mat[row][col+1] < level or \
                                col > 0 and mat[row][col-1] < level or \
                                row < rows - 1 and mat[row+1][col] < level or \
                                row > 0 and mat[row-1][col] < level):
                            mat[row][col] += 1
                            found = True
                        
            
        return mat