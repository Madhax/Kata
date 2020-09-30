class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        bestValue = False
        for x in range(len(nums)):
            left = x + 1
            right = len(nums)-1
            while left<right:
                val = nums[x] + nums[left] + nums[right]

                if bestValue is False:
                    bestValue = val
                    
                elif abs(target-bestValue) > abs(target-val):
                    bestValue = val
                    if target==val:
                        target

                if val > target:
                    right = right -1
                else:
                    left = left + 1
                    
        return bestValue
                