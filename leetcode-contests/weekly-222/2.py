from functools import lru_cache
from collections import defaultdict
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        d = defaultdict(int)
        powers = []
        used = set()
        val = 1
        ctr = 0
        for x in range(25):
            powers.append(val)
            val = val * 2
            
            
        for num in deliciousness:
            d[num] += 1
        
        #print(powers)
        for num in deliciousness:
            for pval in powers:
                if pval < num :
                    continue
                    
                complement = pval - num
                if complement > num:
                    continue
                
                if num == complement and d[complement] >= 2 and num not in used:
                    #print(num, complement, comb(d[complement],2))
                    ctr += comb(d[complement],2)
                    used.add(num)
                    #d[complement] -= 1
                    
                elif d[complement] > 0 and num != complement:
                    #print(num, complement, d[complement])
                    ctr += (d[complement])
                    #used.add(complement)
                    #used.add(num)

                
            
        return ctr % (10**9 + 7)