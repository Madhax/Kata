from sortedcontainers import SortedList

class Solution(object):
    def furthestBuilding(self, A, bricks, ladders):
        N = len(A)
        deltas = []
        for i in xrange(len(A) -  1):
            d = A[i + 1] - A[i]
            if d < 0: deltas.append(0)
            else: deltas.append(d)
        
        def possible(T):
            B = sorted(deltas[:T])
            l = ladders
            while B and l:
                B.pop()
                l -= 1
            return sum(B) <= bricks
        
        # print([possible(x) for x in range(len(deltas))])
        lo = 0
        hi = len(deltas)
        while lo < hi:
            mi = lo +hi +1 >> 1
            if possible(mi):
                lo = mi
            else: hi = mi - 1
        return lo
