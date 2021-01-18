class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        def recurse(level, a, e, i, o, u):
            nonlocal n
            if level == n:
                return sum([a,e,i,o,u])
            
            else:
                return recurse(level+1, a+e+i+o+u, e+i+o+u, i+o+u, o+u, u)
                
        return recurse(1, 1, 1, 1, 1, 1)