class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        bestVertical = 0
        bestHorizontal = 0
        
        for x in range(1, len(horizontalCuts)):
            bestHorizontal = max(bestHorizontal, horizontalCuts[x]-horizontalCuts[x-1])
            
        for x in range(1, len(verticalCuts)):
            bestVertical = max(bestVertical, verticalCuts[x]-verticalCuts[x-1])

        #print(bestHorizontal, bestVertical)
        return (bestHorizontal * bestVertical) % ((10**9) + 7)