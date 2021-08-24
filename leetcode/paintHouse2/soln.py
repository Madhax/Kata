class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        @functools.cache
        def dp(index, prevColor):
            if index == len(costs):
                return 0
            
            best = math.inf
            
            for x in range(0, len(costs[0])):
                if x == prevColor:
                    continue
                    
                best = min(best, costs[index][x] + dp(index+1, x))
                
            return best
            
        return dp(0, None)