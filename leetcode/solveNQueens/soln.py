class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        usedRows = set()
        
        work = [["." for _ in range(n)] for _ in range(n)]
        
        def isSafe(row, col):
            
            if row in usedRows:
                return False
            
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if work[i][j] == "Q":
                    return False
            
            for i, j in zip(range(row, n), range(col, -1, -1)):
                if work[i][j] == "Q":
                    return False
                
            return True
        
        def addOutput():
            cand = []
            for item in work:
                cand.append("".join(item))
            
            output.append(cand)
            
        
        def backTrack(col):
            
            if col >= n:
                addOutput()
                return
                
            for r in range(n):
                if isSafe(r, col):
                    work[r][col] = 'Q'
                    usedRows.add(r)
                    backTrack(col+1)
                    usedRows.remove(r)
                    work[r][col] = '.'
                    
                    
                
        
        backTrack(0)
        
        return output
                
            