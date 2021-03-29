class Solution:
    def secondHighest(self, s: str) -> int:
        
        a = []
        for x in s:
            if x.isdigit() and x not in a:
                a.append(x)
                
        a.sort()
        if len(a) > 1:
            return int(a[-2])
        else:
            return -1