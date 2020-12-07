class Solution:
    def concatenatedBinary(self, n: int) -> int:
        retval = 0
        
        iter = 1
        binStr = ""
        while iter <= n:
            binStr += "{0:b}".format(iter)
            iter += 1
            
        return int(binStr, 2) % (10**9 + 7)