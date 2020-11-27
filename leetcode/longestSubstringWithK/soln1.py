class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        #2 changing variables
        #posn
        #len
       
        #if len matches criteria where each value is K>
        bestFound = 0
       
        x = 0
        slen = len(s)
        while x < slen:
            d = {}
            if len(s) - x < bestFound:
                break
               
            y = x
            leap = bestFound
            while y < slen:
                if s[y] not in d:
                    d[s[y]] = 1
                else:
                    d[s[y]] += 1
                leap -= 1
                if leap > 0:
                    y += 1
                    continue
               
                if (y-x+1) > bestFound:
                    #get how many values below K
                    below = [x for x in d.values() if x < k and x != 0]
                    if len(below) > 0:
                        leap = k*len(below) - sum(below)
                    else:
                        bestFound = (y-x+1)                      
               
                y += 1
               
            x += 1
               
        return bestFound