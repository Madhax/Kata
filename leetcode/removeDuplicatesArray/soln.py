class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        while x < len(nums):
            if nums[x] == nums[x-1]:
                nums.pop(x)
            else:
                x += 1