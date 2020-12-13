from collections import deque
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        
        deck = deque(stones)
        bestAlice = [float("-inf")] * 1000
        bestBob = [float("-inf")] * 1000
        
        
        @lru_cache(maxsize=10000)
        def playGame(currentScore, aliceScore, bobScore, aliceTurn):
            nonlocal deck, bestBob, bestAlice
            
            
            if currentScore == 0:
                #print(aliceScore, bobScore, aliceTurn)
                return abs(aliceScore-bobScore)
            """
            if aliceTurn:
                if bestAlice[len(deck)] > aliceScore:
                    return aliceScore
                
                bestAlice[len(deck)] = aliceScore
                
            else:
                if bestBob[len(deck)] > bobScore:
                    return bobScore
                
                bestBob[len(deck)] = bobScore
                
            """
            
            
            #popleft
            stone = deck.popleft()
            if aliceTurn:
                score1 = playGame(currentScore-stone, aliceScore + (currentScore-stone), bobScore, not aliceTurn)
            else:
                score1 = playGame(currentScore-stone, aliceScore, bobScore + (currentScore-stone), not aliceTurn)
            deck.appendleft(stone)
            
            #popright
            
            stone = deck.pop()
            if aliceTurn:
                score2 = playGame(currentScore-stone, aliceScore + (currentScore-stone), bobScore, not aliceTurn)
            else:
                score2 = playGame(currentScore-stone, aliceScore, bobScore + (currentScore-stone), not aliceTurn)
            deck.append(stone)
            
            if aliceTurn:
                return max(score1, score2)
            else:
                return min(score1, score2)
        
        currentScore = sum(stones)
        
        return playGame(currentScore, 0, 0, True)