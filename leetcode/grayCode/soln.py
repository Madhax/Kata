class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        
        s = []
        grayCode = []
        used = set()
        
        def isOffByOne(x, y):
            for z in range(n):
                if (1<<z) ^ x == y:
                    return True
                
            return False
        
        def recurse(prev):
            nonlocal grayCode
            if len(s) == (2**n - 1):
                prev = s[-1]
                for x in range(n):
                    cand = (1<<x) ^ prev
                    if cand not in used and isOffByOne(cand, s[0]):
                        s.append(cand)
                        #print("here", grayCode)
                        grayCode = s.copy()
                        return True    
                
                return False
            
            for x in range(n):
                cand = (1<<x)^prev
                if cand not in used:
                    used.add(cand)
                    s.append(cand)
                    if recurse(cand):
                        return True
                    s.pop()
                    used.remove(cand)
                    
            return False
    
        #print(isOffByOne(3,2))
        used.add(0)
        s.append(0)
        recurse(0)
        return grayCode