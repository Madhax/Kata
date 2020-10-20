from fractions import gcd
class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        arr = map(int, s)
        n = len(s)
        a = gcd(10, a)
        b = gcd(n, b)
        best = arr
        def best_shift(d):
            r = (d, 0)
            for i in xrange(0, 10, a):
                r = min(r, ((d+i)%10, i))
            return r[1]
        for i in xrange(0, n, b):
            tmp = arr[i:] + arr[:i]
            even_shift = best_shift(tmp[0]) if b % 2 else 0
            odd_shift = best_shift(tmp[1])
            for i in xrange(n):
                tmp[i] += odd_shift if i % 2 else even_shift
                tmp[i] %= 10
            best = min(best, tmp)
        return ''.join(str(d) for d in best)
