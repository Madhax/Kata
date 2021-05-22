class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
#         Approach 1 - leetcode solution: time = O(N!) ; space = O(N)
#         def could_place(row, col):
#             return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
#         def place_queen(row, col):
#             queens.add((row, col))
#             cols[col] = 1
#             hill_diagonals[row - col] = 1
#             dale_diagonals[row + col] = 1
        
#         def remove_queen(row, col):
#             queens.remove((row, col))
#             cols[col] = 0
#             hill_diagonals[row - col] = 0
#             dale_diagonals[row + col] = 0
        
#         def add_solution():
#             solution = []
#             for _, col in sorted(queens):
#                 solution.append('.' * col + 'Q' + '.' * (n - col - 1))
#             output.append(solution)
        
#         def backtrack(row = 0):
#             for col in range(n):
#                 if could_place(row, col):
#                     place_queen(row, col)
#                     if row + 1 == n:
#                         add_solution()
#                     else:
#                         backtrack(row + 1)
#                     remove_queen(row, col)
        
#         cols = [0] * n
#         hill_diagonals = [0] * (2 * n - 1)
#         dale_diagonals = [0] * (2 * n - 1)
#         queens = set()
#         output = []
#         backtrack()
#         return output



# approach 2, refer - https://leetcode.com/problems/n-queens/discuss/19971/Python-recursive-dfs-solution-with-comments.

        d1 = [False]*(2*n -1)
        d2 = [False]*(2*n -1)
        c = [False]*n
        
        res = []
        
        def solve(i, tmp):
            if i == n:
                res.append(list(tmp))
                return
            
            st = ''
            for j in range(n):
                if not c[j] and not d1[i+j] and not d2[i-j]:
                    c[j] = d1[i+j] = d2[i-j] = True
                    st = '.'*j + 'Q' + '.'*(n-j-1)
                    tmp.append(st)
                    solve(i+1, tmp)
                    c[j] = d1[i+j] = d2[i-j] = False
                    tmp.pop()
        
        solve(0, [])
        return res