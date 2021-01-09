class Solution(object):
    def minimumDeviation(self, A):
        A.sort()
        from heapq import heappop,heappush, heapify
        pq = []
        for x in A:
            if x % 2:
                x *= 2
            pq.append(-x)
        heapify(pq)
        m = -max(pq)
        ans = float('inf')
        while True:
            x = -heappop(pq)
            cand = x-m
            if cand<ans:ans=cand
            if x & 1:
                break
            x >>= 1
            if x < m: m = x
            # print("!", max(-x for x in pq), m)
            heappush(pq, -x)
        
        return ans
