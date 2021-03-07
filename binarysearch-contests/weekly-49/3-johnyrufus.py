class Solution:
    def solve(self, a):
        def add_eligible_to_heap(cur):
            if cur is not None:
                tprev, tnex = prev[cur], nex[cur]
                if tprev is None and tnex is None:
                    heappush(heap, (a[cur], cur))
                elif tprev is None and a[cur] > a[tnex]:
                    heappush(heap, (a[cur], cur))
                elif tnex is None and a[cur] > a[tprev]:
                    heappush(heap, (a[cur], cur))
                elif tprev is not None and tnex is not None and a[tprev] < a[cur] > a[tnex]:
                    heappush(heap, (a[cur], cur))

        n = len(a)
        if n in [0, 1]:
            return a

        res, heap = [], []
        prev, nex = dict(), dict()

        prev[0], nex[0] = None, 1
        prev[n - 1], nex[n - 1] = n - 2, None
        for i in range(1, n - 1):
            prev[i] = i - 1
            nex[i] = i + 1

        for i in range(n):
            add_eligible_to_heap(i)

        while heap:
            val, i = heappop(heap)
            res.append(val)

            prev[nex[i]] = prev[i]
            nex[prev[i]] = nex[i]

            for cur in (prev[i], nex[i]):
                add_eligible_to_heap(cur)

        return res
