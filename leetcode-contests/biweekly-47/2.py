class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        seen = set()
        
        @functools.cache
        def recurse(val):
            nonlocal seen
            if val == 0:
                return True
            
            
            for x in range(ceil(log(n, 3))+1):
                if x in seen:
                    continue
                seen.add(x)
                if recurse(val - 3**x):
                    return True
                seen.remove(x)
            return False
        
        return recurse(n)
                
            