class Solution:
    def solve(self, nums):
        best = 0
        i = 0
        curMin = float("inf")
        curMax = float("-inf")
        while i < len(nums):
            j = i
            curMin = nums[i]
            curMax = nums[i]
            while j < len(nums):
                curMin = min(curMin, nums[j])
                curMax = max(curMax, nums[j])

                if curMax - curMin == j - i and (j - i + 1) > best:
                    best = (j - i) + 1

                j += 1

            i += 1

        return best
