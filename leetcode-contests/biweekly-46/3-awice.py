#bfs
class Solution(object):
    def highestPeak(self, A):
        queue = []
        R,C= len(A),len(A[0])
        for r,row in enumerate(A):
            for c, v in enumerate(row):
                if v == 1:
                    queue.append((r,c, 0))
        seen = {(r,c) for r,c,v in queue}
        for r,c,v in queue:
            A[r][c] = v
            for nr, nc in ((r-1,c), (r,c-1), (r+1,c),(r,c+1)):
                if 0<=nr<R and 0<=nc<C and (nr,nc) not in seen:
                    seen.add((nr, nc))
                    queue.append((nr, nc, v + 1))
        return A