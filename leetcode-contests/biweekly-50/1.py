class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ops = 0
        for x in range(1, len(nums)):
            if nums[x] <= nums[x-1]:
                ops += (nums[x-1]-nums[x]+1)
                nums[x] += (nums[x-1]-nums[x]+1)
        return ops