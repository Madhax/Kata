class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        nums_max = nums[0]
        allMax = nums[0]
        solution = 1
        for i in range(1, len(nums)):
            if nums[i] < nums_max:
                solution = i + 1
                nums_max = allMax
            else:
                allMax = max(allMax, nums[i])
        return solution