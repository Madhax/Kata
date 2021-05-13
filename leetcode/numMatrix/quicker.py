class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = []
        prev = [0] * len(matrix[0])
        for row in matrix:
            total = 0
            curr = []
            for i, val in enumerate(row):
                total = total + val
                curr.append(total + prev[i])
            self.prefix_sum.append(curr)
            prev = curr
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0:
            top = 0
        else:
            top = self.prefix_sum[row1-1][col2]
            
        if col1 == 0:
            left = 0
        else:
            left = self.prefix_sum[row2][col1-1]
        
        if row1 == 0 or col1 == 0:
            top_left = 0
        else:
            top_left = self.prefix_sum[row1-1][col1-1]
            
        return self.prefix_sum[row2][col2] - top - left + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)