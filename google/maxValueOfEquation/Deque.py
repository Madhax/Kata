    def findMaxValueOfEquation(self, A, k):
        q = collections.deque()
        res = -float('inf')
        for x, y in A:
            while q and q[0][1] < x - k:
                q.popleft()
            if q: res = max(res, q[0][0] + y + x)
            while q and q[-1][0] <= y - x:
                q.pop()
            q.append([y - x, x])
        return res