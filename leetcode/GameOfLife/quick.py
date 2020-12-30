class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        p=[[0]*(len(board[0])+1) for _ in range(len(board)+1)]
        for r in range(len(board)):            
            for c in range(len(board[r])):
                p[r+1][c+1]=p[r+1][c]+p[r][c+1]-p[r][c]+board[r][c]
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                aa,bb,cc,dd=r+2,c+2,r-1,c-1
                if aa>=len(p): aa=r+1
                if bb>=len(p[aa]): bb=c+1
                if cc<0: cc=r
                if dd<0: dd=c              
                
                x=p[aa][bb]-p[aa][dd]-p[cc][bb]+p[cc][dd]
                                
                if board[r][c]:
                    if x<3 or x>4: board[r][c]=0
                else:
                    if x==3: board[r][c]=1
                
                    
        
        
        #live-> 2/3 neighbor -> live 
        #dead-> 3live ->live
        
        """
        Do not return anything, modify board in-place instead.
        """
