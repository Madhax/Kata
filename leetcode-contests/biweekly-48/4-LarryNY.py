class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)
        
        g = [[-1] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                g[x][y] = math.gcd(nums[x], nums[y])
        
        @lru_cache(None)
        def go(i, mask):
            if mask == 0:
                return 0
            
            best = 0
            for x in range(N):
                if (mask & (1 << x)) > 0:
                    for y in range(x + 1, N):
                        if (mask & (1 << y)) > 0:
                            score = i * g[x][y] + go(i + 1, mask ^ (1 << x) ^ (1 << y))
                            if score > best:
                                best = score
            return best
        return go(1, (1 << N) - 1)