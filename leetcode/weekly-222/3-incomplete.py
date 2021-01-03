from functools import lru_cache
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        index = 0
        
        dpsum = {}
        
        mysum = 0
        for index, num in enumerate(nums):
            mysum += num
            dpsum[index] = mysum
            
        index = 0
        
        #@lru_cache(maxsize=None)
        def dp(minimum, level):
            nonlocal index, nums, dpsum
            #print(level, index, minimum)
            #
            if level == 3 and index < len(nums) and dpsum[index] >= minimum:
                #print("HERE", level, index, minimum)
                return 1
            
            mymin = 0
            ctr = 0
            startindex = index
            while index < len(nums):
                mymin += nums[index]
                index += 1
                if mymin >= minimum:
                    ctr += dp(mymin, level+1)
                
            index = startindex
            #print(ctr)
            return ctr
            
            
            
            
        return dp(0, 1) % (10**9 + 7)