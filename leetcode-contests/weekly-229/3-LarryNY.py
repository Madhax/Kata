class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        M = len(multipliers)
        N = len(nums)
            
        dp = [[-1000000000] * (M + 1) for _ in range(M + 1)]
        
        for i in range(M):
            for left in range(i+1):
                if i == 0:
                    dp[i][left] = 0
                right = N - i + left - 1
                
                score = dp[i][left]
                dp[i + 1][left + 1] = max(dp[i + 1][left + 1], score + nums[left] * multipliers[i])
                dp[i + 1][left] = max(dp[i + 1][left], score + nums[right]  * multipliers[i])
             
        #print(dp)
        return max(dp[M])