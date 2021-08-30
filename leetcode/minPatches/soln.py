class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        miss = 0
        ctr = 1
        i = 0
        while ctr <= n:
            if i < len(nums) and nums[i] <= ctr:
                ctr += nums[i]
                i += 1
            else:
                miss += 1
                ctr += ctr
                
        return miss
                