class Solution:
    def solve(self, s, target):
        n = len(s)
        s = [int(c) for c in s]

        # For each index, precompute the index of the next nonzero digit.
        last = n
        next_nonzero = [0] * n
        for i in reversed(range(n)):
            if s[i] != 0:
                last = i
            next_nonzero[i] = last

        # Pick an arbitrary "bad" solution. We won't consider any solution worse than this one.
        baseline = abs(target - sum(s))

        @cache
        def dp(i, t):
            if i == n:
                # base case
                return abs(t)
            if s[i] == 0:
                # Skip leading zeroes, as they always contribute nothing.
                return dp(next_nonzero[i], t)

            ans = baseline
            cur = 0
            for j in range(i, n):
                cur = cur * 10 + s[j]
                if cur >= t + baseline:
                    break
                if j == n - 1 or cur != 0:
                    ans = min(ans, dp(j + 1, t - cur))
            return ans

        return dp(0, target)
