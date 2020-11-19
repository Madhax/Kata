class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        answer = []
        start, end = intervals[0][0], intervals[0][1]
        for i in intervals[1:]:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                answer.append([start, end])
                start, end = i[0], i[1]
        answer.append([start, end])
        return answer