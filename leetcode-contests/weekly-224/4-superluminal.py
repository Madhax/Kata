class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        # if there is winning solution, it's length is probably very short (<100)
        a = grid
        n, m = len(a), len(a[0])
        mpos = cpos = fpos = -1
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] == 'M': mpos = i*m + j
                elif a[i][j] == 'C': cpos = i*m + j
                elif a[i][j] == 'F': fpos = i*m + j
        def traj(i, j, d):
            if grid[i][j] == '#': return []
            pos = i*m+j
            nei = [pos]
            for k in xrange(1, d+1):
                if i+k>=n or grid[i+k][j]=='#': break
                nei.append(pos+k*m)
            for k in xrange(1, d+1):
                if i-k<0 or grid[i-k][j]=='#': break
                nei.append(pos-k*m)
            for k in xrange(1, d+1):
                if j+k>=m or grid[i][j+k]=='#': break
                nei.append(pos+k)
            for k in xrange(1, d+1):
                if j-k<0 or grid[i][j-k]=='#': break
                nei.append(pos-k)
            return nei
        mnei = [traj(i, j, mouseJump) for i in xrange(n) for j in xrange(m)]
        cnei = [traj(i, j, catJump) for i in xrange(n) for j in xrange(m)]
        k = n * m
        lim = 100
        cache = [[-1]*(k*k) for _ in xrange(lim)]
        def mouse_win(mpos, cpos, turn):
            if turn == lim: return 0
            e = mpos*k+cpos
            if cache[turn][e] >= 0:
                return cache[turn][e] == 1
            if cpos == fpos or cpos == mpos: return 0
            if mpos == fpos: return 1
            if turn & 1: # cat turn
                if all(mouse_win(mpos, newcpos, turn+1) for newcpos in cnei[cpos]):
                    cache[turn][e] = 1
                else:
                    cache[turn][e] = 0
            else: # mouse turn
                if any(mouse_win(newmpos, cpos, turn+1) for newmpos in mnei[mpos]):
                    cache[turn][e] = 1
                else:
                    cache[turn][e] = 0
            return cache[turn][e] == 1
        return mouse_win(mpos, cpos, 0)
