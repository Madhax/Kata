class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #range(max(x[0], y[0]), min(x[-1], y[-1])+1)
        merging = True
        while merging:
            merging = False
            x = 0
            while x < len(intervals):
                y = x + 1
                while y < len(intervals):
                    if len(range(max(intervals[x][0], intervals[y][0]), min(intervals[x][-1], intervals[y][-1])+1)) > 0:
                        intervals[x][0] = min(intervals[x][0], intervals[y][0])
                        intervals[x][1] = max(intervals[x][-1], intervals[y][-1])
                        intervals.pop(y)
                        merging = True
                    else:
                        y += 1
                x += 1
        return intervals

