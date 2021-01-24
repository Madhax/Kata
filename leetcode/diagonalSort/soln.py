class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
       
        diagonals = []
       
        def getArray(y, x):
            nonlocal mat
            #print(y, x)
            res = []
            while True:
                if y < len(mat) and x < len(mat[y]):
                    res.append(mat[y][x])
                   
                else:
                    break
                   
                y += 1
                x += 1
               
            return res
       
        def setArray(y, x, arr):
            nonlocal mat
            iter = 0
            while True:
                if y < len(mat) and x < len(mat[y]):
                    mat[y][x] = arr[iter]
                   
                else:
                    break
                y+=1
                x+=1
                iter+=1
       
        for y in range(len(mat)-1, -1, -1):
            diagonals.append(getArray(y, 0))
           
        for x in range(1, len(mat[0])):
            diagonals.append(getArray(0, x))
           
        #print(diagonals)
        for diagonal in diagonals:
            diagonal.sort()
           
        iter = 0
       
        for y in range(len(mat)-1, -1, -1):
            setArray(y, 0, diagonals[iter])
            iter += 1
       
        for x in range(1, len(mat[0])):
            setArray(0, x, diagonals[iter])
            iter +=1
       
        return mat
