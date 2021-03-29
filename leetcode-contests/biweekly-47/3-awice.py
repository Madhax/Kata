class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            count = Counter()
            for j in range(i, n):
                count[s[j]] += 1
                ans += max(count.values()) - min(count.values())
        return ans