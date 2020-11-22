class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x:x[0]-x[1])
        usedup = 0
        ans = 0
        for t in tasks:
            if ans-usedup<t[1]:
                ans = t[1]+usedup
            usedup+=t[0]
        return ans