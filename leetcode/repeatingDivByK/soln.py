class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        d = {}
        responselen = 1
        currentmod = 1
        while True:
            if currentmod % K == 0:
                return responselen
           
            currentmod = (currentmod * 10 + 1) % K
            responselen += 1
            #cycle
            if currentmod in d:
                return -1
            else:
                d[currentmod] = 1
