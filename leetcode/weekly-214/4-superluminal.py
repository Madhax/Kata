class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        n = max(instructions) + 1
        fen = [0] * (n+1)
        c = [0] * n
        def _get(i):
            r = 0
            while i:
                r += fen[i]
                i -= i & -i
            return r
        def _upd(i):
            i += 1
            while i <= n:
                fen[i] += 1
                i += i & -i
        r = 0
        for i, v in enumerate(instructions):
            below = _get(v)
            above = i - c[v] - below
            r += min(below, above)
            _upd(v)
            c[v] += 1
        return r % (10**9 + 7)