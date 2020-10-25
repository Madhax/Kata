from collections import deque
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        arr = heights
        n, m = len(arr), len(arr[0])
        def check(diff):
            vis = [[False]*m for _ in xrange(n)]
            q = []
            def _consider(x,y):
                if vis[x][y]: return
                q.append((x, y))
                vis[x][y] = True
            _consider(0,0)
            while q:
                x, y = q.pop()
                for xx, yy in (x-1, y), (x, y-1), (x+1, y), (x, y+1):
                    if xx < 0 or yy < 0 or xx >= n or yy >= m: continue
                    if abs(arr[x][y] - arr[xx][yy]) > diff: continue
                    _consider(xx, yy)
            return vis[n-1][m-1]

        a = -1 # imposs
        b = max(val for row in arr for val in row) # poss
        while a + 1 < b:
            c = (a + b) >> 1
            if check(c): b = c
            else: a = c
        return b
