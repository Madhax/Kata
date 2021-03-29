class Solution(object):
    def maxNiceDivisors(self, n):
        MOD = 10 ** 9 + 7
        if n <=4: return n
        if n==5: return 6
        if n==6: return 9
        if n==7: return 12

        q,r = divmod(n-4, 3)
        return pow(3, q, MOD) * self.maxNiceDivisors(r+4) % MOD