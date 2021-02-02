class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        allmax = nums[0]
        curmax = nums[0]
        for i in nums[1:]:
            if curmax + i > i:
                curmax = curmax + i
            else:
                curmax = i
            if curmax > allmax:
                allmax = curmax
                
        return allmax
        
        