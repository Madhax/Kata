
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        cur = 0
        
        for idx, x in enumerate(nums):
            if cur == (total-x):
                return idx
            
            cur += x
            total -= x
        
        return -1