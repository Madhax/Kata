class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        #@functools.cache
        """
        def dp(index, prevVal):
            
            if index == len(nums):
                return 0
            
            val = -math.inf
            #skip
            val = max(val, dp(index + 1, prevVal))
            
            if nums[index] > prevVal:
                print(nums[index], prevVal)
                val = max(val, nums[index] + dp(index+1, nums[index]))
                
            print(index, prevVal, val)
            return val
        
        return dp(0, -math.inf)
        
        """
        
        best = -math.inf
        prev = -math.inf
        cur = 0
        for x in nums:
            if x > prev:
                cur += x
                prev = x
            else:
                best = max(cur, best)
                cur = x
                prev = x
        
        best = max(cur, best)
        return best
