class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        
        def recurse(index, l, r):
            best = math.inf
            
            if index == 3:
                return nums[r] - nums[l]
            
            best = min(best, recurse(index+1, l+1, r))
            best = min(best, recurse(index+1, l, r-1))
            
            return best
            
        return recurse(0, 0, len(nums)-1)