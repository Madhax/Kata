
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col,triple,visited = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set), collections.deque()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    visited.append((i,j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    triple[(i//3,j//3)].add(board[i][j])
        
        def dfs():
            if not visited:
                return True
            r,c = visited[0]
            t = (r//3,c//3)
            for dig in ["1","2","3","4","5","6","7","8","9"]:
                if dig not in row[r] and dig not in col[c] and dig not in triple[t]:
                    board[r][c] = dig
                    row[r].add(dig)
                    col[c].add(dig)
                    triple[t].add(dig)
                    visited.popleft()
                    if dfs():
                        return True
                    else:
                        row[r].discard(dig)
                        col[c].discard(dig)
                        triple[t].discard(dig)
                        visited.appendleft((r,c))
                        board[r][c] = "."
            return False
        dfs()