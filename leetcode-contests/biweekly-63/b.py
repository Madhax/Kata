class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        state = []
        citer = 0
        aliceMoves = 0
        bobMoves = 0
        
        while citer < len(colors):
            cand = colors[citer]

            if cand == "A" and state and state[-1] == "A" and citer+1 < len(colors) and colors[citer+1] == "A":
                aliceMoves += 1

            if cand == "B" and state and state[-1] == "B" and citer+1 < len(colors) and colors[citer+1] == "B":
                bobMoves += 1
            
                      
                
            state.append(cand)
            citer += 1

            
        return aliceMoves > bobMoves
