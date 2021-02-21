class Solution:
    def solve(self, nums):
        nums.sort(reverse=True)

        val1 = nums[0] * nums[1] * nums[2]
        val2 = nums[-1] * nums[-2] * nums[0]

        return max(val1, val2)