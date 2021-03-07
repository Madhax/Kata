class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        x = min(baseCosts)
        if x >= target: return x
        x = 1 + 2*target - x
        f = [0] * x
        for i in baseCosts:
            if i < x: f[i] = 1
        for c in toppingCosts:
            for i in xrange(x-1, c-1, -1): f[i] |= f[i-c]
            for i in xrange(x-1, c-1, -1): f[i] |= f[i-c]
        return min((abs(i-target), i) for i, v in enumerate(f) if v)[1]