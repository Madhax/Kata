class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat[0]) * len(mat):
            return mat
        
        newMat = [[] for _ in range(r)]
        
        rowIter = 0
        colIter = 0
        
        for y in range(r):
            for x in range(c):
                #print(y, x, rowIter, colIter, len(mat[0]))
                newMat[y].append(mat[rowIter][colIter])
                colIter += 1
                if colIter == len(mat[0]):
                    rowIter += 1
                    colIter = 0
                
                
        return newMat