class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        p, q = introvertsCount, extrovertsCount
        if m < n: m, n = n, m
        # col + counts = 11907 sx, 243 tx
        def _dec(x):
            r = []
            for _ in xrange(n):
                r.append(x%3)
                x//=3
            return tuple(r)
        configs = []
        for x in xrange(3**n):
            a = _dec(x)
            b = [0]*n
            for i in xrange(n):
                if a[i] == 0: continue
                if i > 0: b[i-1] += 1
                if i+1 < n: b[i+1] += 1
            score = intro = extro = 0
            for i in xrange(n):
                if a[i] == 1:
                    score += 120 - 30 * b[i]
                    intro += 1
                elif a[i] == 2:
                    score += 40 + 20 * b[i]
                    extro += 1
            configs.append((x, intro, extro, score))
        cross = [[0]*(3**n) for _ in xrange(3**n)]
        for x in xrange(3**n):
            a = _dec(x)
            for y in xrange(3**n):
                b = _dec(y)
                for i in xrange(n):
                    if a[i] == 1 and b[i] == 1:
                        cross[x][y] -= 60
                    elif a[i] == 2 and b[i] == 2:
                        cross[x][y] += 40
                    elif a[i] + b[i] == 3:
                        cross[x][y] -= 10
        f = Counter()
        f[(0, introvertsCount, extrovertsCount)] = 0
        for _ in xrange(m):
            ff = Counter()
            for (x, i, e), s in f.iteritems():
                for xx, ii, ee, ss in configs:
                    if i-ii < 0 or e-ee < 0: continue
                    kk = (xx, i-ii, e-ee)
                    vv = s + ss + cross[x][xx]
                    ff[kk] = max(ff[kk], vv)
            f = ff
        return max(f.itervalues())