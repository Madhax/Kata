class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for _ in range(len(nums))]
        
        for x in range(1, len(nums)):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y]+1)
                
        return max(dp)
        