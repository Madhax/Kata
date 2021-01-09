class Solution(object):
    def bestCoordinate(self, towers, radius):
        ansi = 0,0
        ans = float('-inf')
        def dist2(x1, y1, x2, y2):
            xd = abs(x2-x1)
            yd = abs(y2-y1)
            return xd**2 + yd**2
        def quality(x, y):
            score = 0
            for x0, y0, q0 in towers:
                d2 = dist2(x,y,x0,y0)
                if d2 > radius**2: continue
                score += int(q0 / (1 + d2 ** 0.5))
            return score
        
        for x in xrange(51):
            for y in xrange(51):
                q = quality(x, y)
                if q > ans:
                    ans = q
                    ansi = x, y
        return list(ansi)
