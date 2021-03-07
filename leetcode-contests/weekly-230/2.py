class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        T = len(toppingCosts)
        
        best = math.inf
        bestDiff = math.inf
        def recursive(curVal, toppingIndex):
            nonlocal best, bestDiff
            diff = abs(curVal - target)
            
            #if diff > bestDiff:
            #    return
            
            if toppingIndex >= T:
                
                if diff < bestDiff:
                    best = curVal 
                    bestDiff = diff
                    
                elif diff == bestDiff:
                    if curVal < best:
                        best = curVal
                        
                return

            recursive(curVal + (toppingCosts[toppingIndex]), toppingIndex + 1)
            recursive(curVal , toppingIndex + 1)
            recursive(curVal + ((toppingCosts[toppingIndex])*2), toppingIndex + 1)    
            return
        
        for base in baseCosts:
            recursive(base, 0)
            
        return best