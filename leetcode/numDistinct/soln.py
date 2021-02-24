class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        I = len(s)
        J = len(t)
        
        @functools.cache
        def dp(i, j):
            
            if j == J:
                return 1
            
            if i == I:
                return 0
            
            ret = 0
            
            if s[i] == t[j]:
                ret += dp(i+1, j+1)
                
            ret += dp(i+1, j)
            
            return ret
        
        return dp(0, 0)