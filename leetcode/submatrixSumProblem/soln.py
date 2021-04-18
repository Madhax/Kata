class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M = len(matrix)
        N = len(matrix[0])
       
        #psum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
       
        for y in range(M):
            rowval = 0
            for x in range(1, N):
                matrix[y][x] += matrix[y][x-1]
       
        cnt = 0
       
        for x in range(N):
            for x0 in range(x, N):
                for y in range(0, M):
                    rval = 0
                    for y0 in range(y, M):
                        rval += matrix[y0][x0] - (matrix[y0][x-1] if x else 0)
                        if rval == target:
                            cnt += 1
                       
               
        #print(psum)
        return cnt