class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = collections.Counter(nums)
        res = 0
        for i in counts:
            if i * 2 == k:
                res += math.floor(counts[i]/2)
            elif i <= k/2:
                if k - i in counts:
                    res += min(counts[i],counts[k-i])
        return res