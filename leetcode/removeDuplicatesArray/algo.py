class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        if len(nums) <= 1:
            return len(nums)
        j =0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i] 
                j += 1
        return j+1