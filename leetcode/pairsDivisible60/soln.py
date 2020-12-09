class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ctr = 0
        """
        for x in range(len(time)):
            for y in range(x+1, len(time)):
                if (time[x] + time[y]) % 60 == 0:a
                    ctr += 1
        """
       
        d = {}
        for x in range(60):
            d[x] = 0
           
        for x in range(len(time)):
            complement = time[x]%60
            d[complement] += 1
               
        #print(d)
        for x in range(len(time)):
            mod = (time[x] % 60)
            complement = (60-mod)%60
            d[mod] -= 1    
            ctr += d[complement]
            #print(time[x], mod, d[mod])
           
   
        return ctr