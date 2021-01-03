class Solution(object):
    def countPairs(self, A):
        MOD = 10 **9 + 7
        count = Counter()
        powers = {1 << i for i in range(31)}
        ans = 0
        for x in A:
            for pwr in powers:
                ans += count[pwr - x]
            count[x] += 1
        return ans % MOD