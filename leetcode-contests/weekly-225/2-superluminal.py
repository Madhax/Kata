class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        def cost1(c1, c2):
            cost = sum(c1.itervalues())
            best = float('inf')
            for i in xrange(25):
                cost += c2[i] - c1[i]
                best = min(best, cost)
            return best
        def cost3(c):
            return sum(c.itervalues()) - max(c.itervalues())
        c1 = Counter(ord(ch)-ord('a') for ch in a)
        c2 = Counter(ord(ch)-ord('a') for ch in b)
        return min(cost1(c1, c2), cost1(c2, c1), cost3(c1) + cost3(c2))