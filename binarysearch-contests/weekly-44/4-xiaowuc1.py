class Solution:
    def solve(self, s, target):
        dp = []
        for _ in range(len(s) + 1):
            dp.append(set())
        dp[0].add(0)
        maxseen = [float("inf")] * (len(s) + 1)
        for i in range(len(s)):
            curr = 0
            for j in range(i, len(s)):
                curr = 10 * curr + int(s[j])
                for prev in dp[i]:
                    if prev > maxseen[i]:
                        continue
                    cand = prev + curr
                    if cand >= maxseen[j + 1]:
                        continue
                    dp[j + 1].add(cand)
                    if cand >= target:
                        maxseen[j + 1] = cand
                if curr >= target or curr == 0:
                    break
        ret = float("inf")
        for cand in dp[len(s)]:
            ret = min(ret, abs(target - cand))
        return ret
