class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        M = len(board[0])
        N = len(board)
        
        def isEndpoint(y,x, direction):
            ny = y + direction[0]
            nx = x + direction[1]
            
            if ny < 0 or ny >= N:
                return True
            
            if nx < 0 or nx >= M:
                return True
            
            if board[ny][nx] == ".":
                return True
            
            return False
        
        isValid = False
        
        #check up
        directions = [[-1, 0], [-1, 1], [-1, -1], [1,1], [1,-1], [1,0], [0,-1], [0,1]]
        
        
        for direction in directions:
            if isEndpoint(rMove,cMove, direction):
                continue
            y = rMove + direction[0]
            x = cMove + direction[1]
            cursize = 1
            while True:
                cursize += 1
                
                if color == board[y][x]:
                    if cursize >= 3:
                        return True
                    break
                    
                if isEndpoint(y,x, direction):
                    #if color == board[y][x] and cursize >= 3:
                    #    return True
                    
                    break
                    
                if board[y][x] == ".":
                    break
                    
                y += direction[0]
                x += direction[1]
                
        return False
            
        
