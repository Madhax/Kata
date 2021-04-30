class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        posn = bisect_left(nums, target)
        if posn < len(nums) and nums[posn] == target:
            return [posn, bisect_right(nums, target)-1]
        
        return [-1,-1]