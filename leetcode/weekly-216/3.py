class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def getValues(index):
            nonlocal nums
            if index >= len(nums):
                return 0
            
            return nums[index] + getValues(index+2)
            
            
        odds = 0
        evens = 0
        index = 0
        ctr = 0
        while index < len(nums):
            
            if index % 2 == 0:
                e = getValues(index+1)
                o = getValues(index+2)
                
                if odds+o == evens+e:
                    ctr += 1
                
                evens += nums[index]
                index += 1
            else:
                o = getValues(index+1)
                e = getValues(index+2)
                
                if odds+o == evens+e:
                    ctr += 1
                
                odds += nums[index]
                index += 1
        
        return ctr