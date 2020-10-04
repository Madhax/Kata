from math import atan2, pi
class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        mx, my = location
        ang = pi * angle / 180.  + 1e-6
        c = r = 0
        a = []
        for x, y in points:
            dx, dy = x - mx, y - my
            if dx == dy == 0:
                c += 1
                continue
            th = atan2(dy, dx)
            a.append(th)
            a.append(th + 2*pi)
        a.sort()
        i = 0
        for j in xrange(len(a)):
            while i < j and a[j] - a[i] > ang:
                i += 1
            r = max(r, 1 + j - i)
        return c + r
            
