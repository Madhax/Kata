class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @functools.cache
        
        def dp(step):
            
            if step >= len(cost):
                return 0
            
            return min(cost[step] + dp(step+1), cost[step] + dp(step+2))
    
        return min(dp(0), dp(1))