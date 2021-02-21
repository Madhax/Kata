class Solution:
    def countHomogenous(self, s: str) -> int:
        
        MOD = (10 ** 9) + 7
        
        seq = [''.join(g) for _, g in groupby(s)]
        
        ctr = 0
        """
        @functools.cache
        def myCount(c):
            ctr = 0
            for x in range(1, c+1):
                ctr += c // x

            return ctr
        """
        
       # print(myCount(1))
        #print(myCount(2))
        #print(myCount(3))
        for s in seq:
            ctr += (len(s) * (len(s)+1)) // 2
            #print(s, (len(s) * (len(s)+1)) // 2)
        #print(seq)
        return ctr % MOD