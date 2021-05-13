class NumMatrix:
    def build(self, index, arr):
        n = self.n
        # insert leaf nodes in tree 
        for i in range(len(arr)) : 
            self.segmentTree[index][n + i] = arr[i]; 

        # build the tree by calculating parents 
        for i in range(n - 1, 0, -1) : 
            self.segmentTree[index][i] = self.segmentTree[index][i << 1] + self.segmentTree[index][i << 1 | 1]; 
        
    def query(self, arr, l, r):
        n = self.n
        res = 0; 

        # loop to find the sum in the range 
        l += n;
        r += n;

        while l < r :

            if (l & 1) :
                #print(arr, l)
                res += arr[l]; 
                l += 1

            if (r & 1) :
                r -= 1;
                res += arr[r]; 

            l >>= 1;
            r >>= 1

        return res; 
        
        
        
    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix[0])
        self.segmentTree = [[0 for _ in range(len(matrix[0]) * 2)] for _ in range(len(matrix))]
        
        for index, row in enumerate(matrix):
            self.build(index, row)
            
        #print(self.segmentTree)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #print()
        output = 0
        for row in range(row1, row2+1):
            output += self.query(self.segmentTree[row], col1, col2+1)
            #print(row, col1, col2, self.query(self.segmentTree[row], col1, col2))
        
        return output


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)