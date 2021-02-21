from collections import *
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        @functools.cache
        def maxdp(i):
            nonlocal nums
            
            if i == len(nums):
                return -math.inf
            
            
            ans = nums[i]
            
            return max(ans, ans+maxdp(i+1))
        
        @functools.cache
        def mindp(i):
            nonlocal nums
            
            if i == len(nums):
                return math.inf
            
            
            ans = nums[i]
            
            return min(ans, ans+mindp(i+1))
        
        val1 =  max([maxdp(x) for x in range(len(nums))])
        val2 = min([mindp(x) for x in range(len(nums))])
        
        return max(abs(val1), abs(val2))