class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        best = ""
        x = 0
        while x < len(s):
            inSet = set()
            C  = Counter()
            y = x 
            while y < len(s):
                
                if s[y] not in inSet:
                    inSet.add(s[y])
                    tmp = s[y]
                    tmp = tmp.lower()
                    C[tmp] += 1
                    
                if all(val == 2 for val in C.values()):
                    if (y - x+1) > len(best):
                        best = s[x:y+1]
                            
                    #print(y, x, C)
                            
                #if x == 3:
                #    print(C)
                y += 1
            x += 1
                
        return best