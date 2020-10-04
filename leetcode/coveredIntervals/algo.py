class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if not n:
            return 0
        
        inter = sorted(intervals, key=lambda x: x[0]*10**6-x[1])
        ans = n
        l, r = inter[0]
        for stard, end in inter[1:]:
            if end > r:
                r = end
            elif end <= r:
                ans -= 1
            else:
                l, r = stard, end
            
        return ans