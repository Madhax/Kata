
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        
        results = [[0] * cols for _ in range(rows)]
        
        for y in range(cols):
            x = 0
            while colSum[y] > 0:
                results[x][y] = min(colSum[y], rowSum[x])
                colSum[y] -= results[x][y]
                rowSum[x] -= results[x][y]
                
                x += 1
                
        return results
