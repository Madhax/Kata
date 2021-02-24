class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
       
        if matrix[M-1][N-1] < target:
            return False
       
        for x in range(M):
            if matrix[x][0] <= target:
                posn = bisect.bisect_left(matrix[x], target)
                if posn < N and matrix[x][posn] == target:
                    return True
       
        return False