class Solution:
    def concatenatedBinary(self, n: int) -> int:
        l = ["{0:b}".format(x) for x in range(1, n+1)]
        #print(l)
        binStr = "".join(l)
        return int(binStr, 2) % (10**9 + 7)