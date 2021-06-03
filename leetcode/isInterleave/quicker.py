class Solution:
    def isInterleave(self, s: str, t: str, u: str) -> bool:
        dp = {}
        
        if len(s) + len(t) != len(u):
            return False
        
        
        def tlehelper(i, j, k):
            if i < len(s) and j< len(t):
                if (s[i:], t[j:]) in dp:
                    return dp[(s[i:], t[j:])]
            
                if s[i] == u[k] and t[j] == u[k]:
                    dp[(s[i:],t[j:])] = tlehelper(i+1, j, k+1) or tlehelper(i, j+1, k+1)
                    return dp[(s[i:],t[j:])]
                elif s[i] == u[k]:
                    dp[(s[i:],t[j:])] = tlehelper(i+1, j, k+1)
                    return dp[(s[i:],t[j:])]
                elif t[j] == u[k]:
                    dp[(s[i:],t[j:])] = tlehelper(i, j+1, k+1)
                    return dp[(s[i:],t[j:])]
                else:
                    return False
            elif i < len(s):
                return s[i:] == u[k:]
            else:
                return t[j:] == u[k:]
            
        return tlehelper(0, 0, 0)