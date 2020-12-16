class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        count=1
        begin=points[0][1]
        for start,end in points:
            if start >begin:
                count+=1
                begin=end
        return count