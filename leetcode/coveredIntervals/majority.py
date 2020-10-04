class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > left and intervals[i][1] > right:
                ans += 1
                left = intervals[i][0]
                right = intervals[i][1]
            else:
                right = max(right, intervals[i][1])
        ans += 1
        return ans