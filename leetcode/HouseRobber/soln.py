from functools import *
class Solution:
    nums = []
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.length = len(nums)
        @lru_cache
        def GetMaxStolen(offset, first):
            if offset >= self.length:
                return 0
            
            elif offset < self.length-1:
                lval = self.nums[offset] + GetMaxStolen(offset+2, first)
                rval = GetMaxStolen(offset+3, first)
                if offset < self.length-2 and first:
                    rval += self.nums[offset+1]
                return max(lval, rval, GetMaxStolen(offset+1, first))
            elif not first:
                return self.nums[offset]
            else:
                return 0
            
        if len(nums) > 1:
            return max(nums[0] + GetMaxStolen(2, True), GetMaxStolen(1, False))
        elif len(nums) == 1:
            return nums[0]
        else:
            return 0