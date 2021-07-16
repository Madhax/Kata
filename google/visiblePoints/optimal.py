class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def points_to_degrees(start, points):
            sx,sy = start
            l = []
            offset = 0
            for x,y in points:
                if x == sx and y == sy:
                    offset +=1
                else:
                    l.append((math.degrees(math.atan2(y-sy, x-sx))+360)%360)
            return offset, l

        def solve(degs, angle):
            max_count = 0
            for i in range(len(degs)):
                # we dont need to binsearch what we've seen
                if i > 0 and degs[i-1] == degs[i]:continue
                end_idx = bisect_right(degs, (degs[i]+angle)%360)
                # if we have come more than full circle 
                if end_idx <= i:
                    count = len(degs)-i+end_idx
                else:
                    count = end_idx-i
                max_count = max(max_count, count)
            return max_count

        offset, degs = points_to_degrees(location, points)
        return offset+solve(sorted(degs), angle)