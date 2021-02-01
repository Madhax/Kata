class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        d = Counter()
        c = Counter()
        for u, v in adjacentPairs:
            d[u] ^= v
            d[v] ^= u
            c[u] += 1
            c[v] += 1
        a, b = [k for k, v in c.iteritems() if v == 1]
        r = [a]
        prev = 0
        while a != b:
            prev, a = a, d[a] ^ prev
            r.append(a)
        return r