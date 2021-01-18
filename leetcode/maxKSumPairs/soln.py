from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter()
        ops = 0
        for num in nums:
            if c[k-num] > 0:
                c[k-num] -= 1
                ops += 1
            else:
                c[num] += 1
        return ops