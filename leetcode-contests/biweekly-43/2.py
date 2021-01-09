class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        #print(s,x,y)
        
        if x >= y:
            offset = s.find("ab", 0)
            while offset >= 0:
                score += x
                s = s[0:offset] + s[offset+2:]
                offset = s.find("ab", max(0,offset-2))
            
            offset = s.find("ba", 0)
            while offset >= 0:
                score += y 
                s = s[0:offset] + s[offset+2:]
                offset = s.find("ba", max(0,offset-2))

        
        else:
            
            offset = s.find("ba", 0)
            while offset >= 0:
                score += y 
                s = s[0:offset] + s[offset+2:]
                offset = s.find("ba", max(0,offset-2))

                
            
            offset = s.find("ab", 0)
            while offset >= 0:
                score += x
                s = s[0:offset] + s[offset+2:]
                offset = s.find("ab", max(0,offset-2))
                    
        return score