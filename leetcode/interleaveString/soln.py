class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        I = len(s1)
        J = len(s2)
        K = len(s3)
        
        if I + J != K:
            return False
        
        @functools.cache
        def dp(i,j):
            k = i + j
            #print(i,j,k, I, J, K)
            if i == I and j == J and k == K:
                return True
            
            ret = False
            
            if i < len(s1) and s1[i] == s3[k]:
                ret = dp(i+1, j)
                if ret == True:
                    return True
            
            if j < len(s2) and s2[j] == s3[k]:
                ret = dp(i, j+1)
                if ret == True:
                    return True
            
            return ret
    
        return dp(0,0)