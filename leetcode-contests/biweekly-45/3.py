class Solution:
    def minimumLength(self, s: str) -> int:
        
        self.best = math.inf
        """
        @functools.cache
        def dp(i, j):
            
            if j - i < self.best:
                return self.best
            
            prefixset = set()
            
            for x in range(i , j):
                prefixset.add(s[i])
                
                suffixset = set()
                for y in range(j, i, -1):
                    if x > y:
                        continue
                        
                    suffixset.add(s[y])
                    if suffixset != prefixset:
                        continue
                    
            
            #pick prefix
            #pick suffix
            #dp deeper
            """
        
        while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
                
        #print(s)
        return len(s)
        #dp(0, len(s))
        #return min(self.best, len(s))