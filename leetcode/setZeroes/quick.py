class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        idx1 = []
        idx2 = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i not in idx1:
                        idx1.append(i)
                    if j not in idx2:
                        idx2.append(j)
        print(idx1,idx2)
        for i in idx1:
            matrix[i][:] = [0]*len(matrix[i])
        
        for i in range(len(matrix)):
            for j in idx2:
                matrix[i][j]=0