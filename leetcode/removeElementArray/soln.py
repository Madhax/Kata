class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        while x < len(nums):
            if nums[x] == val:
                nums.pop(x)
            else:
                x+=1