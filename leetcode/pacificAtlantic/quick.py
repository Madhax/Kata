class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return matrix
        pac = set()
        atl = set()
        def dfs(row,col,isPac):
            q = deque()
            q.append((row,col))
            if isPac:
                temp = pac
            else:
                temp = atl
            while q:
                row,col = q.pop()
                if isPac:
                    pac.add((row,col))
                else:
                    atl.add((row,col))
                if row > 0 and (row-1,col) not in temp and matrix[row-1][col] >= matrix[row][col]:
                    q.append((row-1,col))
                if col > 0 and (row,col-1) not in temp and matrix[row][col-1] >= matrix[row][col]:
                    q.append((row,col-1))
                if row < len(matrix)-1 and (row+1,col) not in temp and matrix[row+1][col] >= matrix[row][col]:
                    q.append((row+1,col))
                if col < len(matrix[0])-1 and (row,col+1) not in temp and matrix[row][col+1] >= matrix[row][col]:
                    q.append((row,col+1))

        for row in range(len(matrix)):
            if not (row,0) in pac:
                dfs(row,0,True)
        for row in range(len(matrix)):
            if not (row,len(matrix[0]) - 1) in atl:
                dfs(row,len(matrix[0]) - 1,False)
        for col in range(len(matrix[0])):
            if not (0,col) in pac:
                dfs(0,col,True)
        for col in range(len(matrix[0])):
            if not (len(matrix)-1,col) in atl:
                dfs(len(matrix)-1,col,False)
        res = []
        for p in pac:
            if p in atl:
                res.append(list(p))
        return res