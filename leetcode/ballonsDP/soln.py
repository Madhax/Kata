class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #prefer smaller balloons
        
        #optimization problem requiring dp
        
        #which balloon to burst
        extended = [1] + nums + [1]
        memo = [[0] * (len(nums) + 2) for x in range(len(nums) + 2)]

        @lru_cache(maxsize=None)
        def dp(left, right):
            nonlocal extended, memo
            
            if left == right:
                return 0

            if memo[left][right] > 0:
                return memo[left][right]
            
            bestOutcome = 0
            for x in range(left + 1, right):
                bestOutcome = max(bestOutcome, extended[left] * extended[x] * extended[right] + dp(left, x) + dp (x, right))
            
            memo[left][right] = bestOutcome
            return bestOutcome
        
        return dp(0, len(nums)+1)
        
        
            