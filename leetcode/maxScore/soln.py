class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        maxScore = 0
        curScore = 0
        
        for x in range(k):
            curScore += cardPoints[x]
            
        j = 0
        maxScore = max(curScore, maxScore)
        #print(curScore)
        while j < k:
            #print(curScore, j, cardPoints[k-j-1], cardPoints[-(j+1)])
            curScore -= cardPoints[k-j-1]
            curScore += cardPoints[-(j+1)]
            j += 1
            maxScore = max(curScore, maxScore)
        
        return maxScore
            