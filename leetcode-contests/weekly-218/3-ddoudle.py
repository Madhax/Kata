class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = 0
        prev = 0
        mul = 1
        for i in range(1, n+1):
            l = len(bin(i))-2
            if l > prev:
                mul *= 2
                mul %= mod
            prev = l
            res *= mul
            res %= mod
            res += i
        return res