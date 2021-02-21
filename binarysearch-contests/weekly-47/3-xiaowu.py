class Solution:
    def solve(self, points):
        ret = [inf] * len(points)
        xtoy = defaultdict(list)
        ytox = defaultdict(list)
        n = len(points)
        for i in range(n):
            xtoy[points[i][0]].append((points[i][1], i))
            ytox[points[i][1]].append((points[i][0], i))
        self.update(ret, xtoy)
        self.update(ret, ytox)
        return ret

    def update(self, ret, dp):
        for _, points in dp.items():
            points = sorted(points)
            for i in range(1, len(points)):
                diff = points[i][0] - points[i - 1][0]
                ret[points[i][1]] = min(ret[points[i][1]], diff)
                ret[points[i - 1][1]] = min(ret[points[i - 1][1]], diff)