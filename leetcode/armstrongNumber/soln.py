class Solution:
    def isArmstrong(self, n: int) -> bool:
        strval = str(n)
        k = len(strval)
        return n == sum([int(x)**k for x in strval])