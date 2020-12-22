class Solution:
    def smallestRangeII(self, a: List[int], k: int) -> int:
        a.sort()
        ans = a[-1] - a[0]
        for x, y in zip(a, a[1:]):
            ans = min(ans, max(a[-1]-k, x+k) - min(a[0]+k, y-k))
        return ans