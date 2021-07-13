class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        as1 = []
        at = []
        
        sd = {}
        td = {}
        
        si = 0
        ti = 0
        
        for c in s:
            if c in sd:
                as1.append(sd[c])
                
            else:
                sd[c] = si
                as1.append(sd[c])
                si += 1
                
        for c in t:
            if c in td:
                at.append(td[c])
                
            else:
                td[c] = ti
                at.append(td[c])
                ti += 1
                
        #print(as1, at)
        
        return as1 == at