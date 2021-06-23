from bisect import *

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        d = defaultdict(list)
        for idx, c in enumerate(s):
            d[c].append(idx)
        
        ctr = 0
        for q in words:
            posn = 0
            invalid = False
            for c in q:
                posn = bisect_left(d[c], posn)
                #print(posn, d[c])
                if len(d[c]) <= posn:
                    invalid = True
                    break
                posn = d[c][posn]+1
            
            if invalid == False:
                ctr += 1
        
        return ctr