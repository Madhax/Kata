import bisect
class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:

        start, end, profit = zip(*sorted(zip(start, end, profit)))
        jump = {i: bisect.bisect_left(start, end[i]) for i in range(len(start))}

        @functools.lru_cache(None)
        def helper(i):
            if i == len(start): return 0
            return max(helper(i+1), profit[i] + helper(jump[i]))

        return helper(0)