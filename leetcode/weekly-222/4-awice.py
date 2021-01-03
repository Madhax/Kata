# from sortedcontainers import SortedList
    
class Solution:
    def minOperations(self, T: List[int], A: List[int]) -> int:
        # tix = {t: i for i,t in enumerate(T)}
        aix = collections.defaultdict(list)
        for i, x in enumerate(A):
            aix[x].append(i)

        dp = [-1]
        for t in T:
            for i in reversed(aix[t]):
                ix = bisect.bisect_left(dp, i)
                if ix >= len(dp): dp.append(-1)
                dp[ix] = i
            
        #     print(dp)
        # print()
        return len(T) + 1 - len(dp)