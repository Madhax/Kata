class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def VerticalValid(col):
            seen = set()
            for x in range(9):
                if board[x][col] == ".":
                    continue
                cand = int(board[x][col])
                if 1 <= cand <= 9 and cand not in seen:
                    seen.add(cand)
                else:
                    return False
                
            return True
            
        def HorizontalValid(row):
            seen = set()
            for x in range(9):
                if board[row][x] == ".":
                    continue
                cand = int(board[row][x])
                if 1 <= cand <= 9 and cand not in seen:
                    seen.add(cand)
                else:
                    return False
                
            return True
            
        def blockValid(row, col):
            seen = set()
            
            for x in range(3):
                for y in range(3):
                    if board[row+y][col+x] == ".":
                        continue
                    cand = int(board[row+y][col+x])
                    if 1 <= cand <= 9 and cand not in seen:
                        seen.add(cand)
                    else:
                        return False
            return True
            
            
        for x in range(9):
            if not (VerticalValid(x) and HorizontalValid(x)):
                return False
            
        
        return True == blockValid(0, 0) == blockValid(0, 3) == blockValid(0, 6) == blockValid(3, 0) == blockValid(3, 3) == blockValid(3, 6) == blockValid(6, 0) == blockValid(6, 3) == blockValid(6, 6)
            
        