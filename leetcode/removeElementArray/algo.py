class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in range(0,len(nums)):
            if nums[x] != val:
                nums[i] = nums[x]
                i += 1
        return i