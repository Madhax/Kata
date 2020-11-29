class Solution(object):
    def minMoves(self, A, limit):
        N = len(A)
        events = [0] * (2 * limit + 3)
        
        def add(lo,hi,v):
            events[lo] += v
            events[hi+1] -= v

        for i in xrange(N // 2):
            x = A[i]
            y = A[~i]
            if x > y: x,y=y,x
            s = x+y
            lo = x + 1
            hi = y + limit
            add(0, 2 * limit + 1, 2)
            add(x + 1, y + limit, -1)
            add(s, s, -1)
            #print("after", events, x, y)
            #B = events[:]
            #for i in xrange(1, len(events)):
            #    B[i] += B[i - 1]
            #print("and", B)
            
        for i in xrange(1, len(events)):
            events[i] += events[i - 1]
        events.pop()
        return min(events)
