class Solution:
    def maxScore(self, a: List[int]) -> int:
        n = len(a)
        scores = [[gcd(x, y) for x in a] for y in a]
        # print(scores)
        @lru_cache(None)
        def dfs(st, mul):
            if mul == 0: return 0
            return max(
                dfs(st - (1 << i) - (1 << j), mul - 1) + mul * scores[i][j]
                for i in range(n)
                for j in range(i+1, n)
                if st & (1 << i) and st & (1 << j)
            )
        ans = dfs((1 << n) - 1, n // 2)
        dfs.cache_clear()
        return ans
        