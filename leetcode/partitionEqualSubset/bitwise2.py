class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2: return False
        k = sum(nums)
        if k%2 or max(nums) > k//2: return False
        dp, k = 1, (1 << (k//2))
        for n in nums:
            dp = dp << n | dp   # Integers in Python 3 are of unlimited size. Python 2 has two integer types - int and long.
            if dp & k:
                return True
        return False   