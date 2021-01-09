class Solution(object):
    def maxProfit(self, A, X):
        A.sort()
        MOD = 10 ** 9 + 7
        
        def cut(t):
            s = 0
            for x in A:
                s += max(0, x-t)
            return s

        lo = 0
        hi = max(A)
        while lo < hi:
            mi = lo + hi + 1 >> 1
            cmi = cut(mi)
            if cmi >= X:
                lo = mi
            else:
                hi = mi - 1
        
        def sumof(n):
            return n * (n + 1) >> 1
        def sumofrange(lo, hi):
            return sumof(hi) - sumof(lo - 1)
        cn = lo
        sold = 0
        profit = 0
        for x in A:
            if cn < x:
                delta = sumofrange(cn + 1, x)
                profit += delta
                sold += x - cn
        
        if sold > X:
            profit -= (cn + 1) * (sold - X)
        # ans = 0
        return profit % MOD
        
