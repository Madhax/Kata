class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for x in reversed(range(len(triangle) - 1)):
            for y in range(len(triangle[x])):
                triangle[x][y] += min(triangle[x + 1][y], triangle[x + 1][y + 1])
        
        return triangle[0][0]