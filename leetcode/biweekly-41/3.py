class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        bestMoves = [x[0] + x[1] for x in zip(aliceValues, bobValues)]
        
        bestMoves = [[x[1], x[0]] for x in enumerate(bestMoves)]
        
        bestMoves.sort(key=lambda x: x[0], reverse=True)
        
        print(bestMoves)
        
        aliceScore = 0
        bobScore = 0
        
        #print(bestMoves)
        aliceTurn = True
        for move in bestMoves:
            #if aliceTurn:
            #bestStone = bestMoves.index(max(bestMoves))
            #else:
            #    bestStone = bestMoves.index(min(bestMoves))
            #print("here", bestStone)
            if aliceTurn:
                aliceScore += aliceValues[move[1]]
                #del aliceValues[bestStone]
                #del bobValues[bestStone]
                #del bestMoves[bestStone]
                aliceTurn = False
                
            else:
                bobScore += bobValues[move[1]]
                #del aliceValues[bestStone]
                #del bobValues[bestStone]
                #del bestMoves[bestStone]
                aliceTurn = True
                
        
        #print(aliceScore, bobScore)
        
        if aliceScore > bobScore:
            return 1
        
        elif aliceScore == bobScore:
            return 0
        
        else:
            return -1
            
            
            