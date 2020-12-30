class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def getLiveNeighbors(y,x):
            nonlocal board
            
            counter = 0
            if y > 0:
                if x > 0:
                    counter += board[y-1][x-1]
                
                counter += board[y-1][x]
                
                if x < len(board[0]) - 1:
                    counter += board[y-1][x+1]
                
            if x > 0:
                counter += board[y][x-1]
                
            if x < len(board[0]) - 1:
                counter += board[y][x+1]
                
            if y < len(board)-1:
                if x > 0:
                    counter += board[y+1][x-1]
                
                counter += board[y+1][x]
                
                if x < len(board[0]) - 1:
                    counter += board[y+1][x+1]
                
            return counter                
                
        actions = []

        for y in range(len(board)):
            for x in range(len(board[0])):
                neighbours = getLiveNeighbors(y,x)
                """
                Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""
                if neighbours < 2:
                    actions.append([y,x,0])
                    
                if neighbours > 3:
                    actions.append([y,x,0])
                
                if neighbours == 3:
                    actions.append([y,x,1])
                    
        for action in actions:
            board[action[0]][action[1]] = action[2]
            
        