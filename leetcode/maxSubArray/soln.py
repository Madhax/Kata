class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        @functools.cache
        def dp(i):
            nonlocal nums
            
            if i == len(nums):
                return -math.inf
            
            
            ans = nums[i]
            
            return max(ans, ans+dp(i+1))
        
        
        return max([dp(x) for x in range(len(nums))])