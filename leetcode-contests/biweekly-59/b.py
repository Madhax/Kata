class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        negCount = 0
        absMin = math.inf
        vals = []
        
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] < 0:
                    negCount += 1
                absMin = min(absMin, abs(matrix[y][x]))
                vals.append(abs(matrix[y][x]))
        
        vals.sort()
        #print(vals)
        return sum(vals) if negCount % 2 == 0 else sum(vals[1:]) - vals[0]