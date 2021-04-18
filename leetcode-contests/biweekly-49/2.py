class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            
        """
        isBuilding = False
        
        s1iter, s2iter = 0, 0
        
        while s1iter < len(s1) or s2iter < len(s2):
            
            if s1[s1iter] == s2[s2iter]
        """
        @functools.cache
        def dp(i1, i2, isBuilding, hasBuilt):
            if i1 > len(s1):
                return False
            
            if i2 > len(s2):
                return False
            
            if i1 == len(s1) and i2 == len(s2):
                return True
            
            ret = False
            
            if i1 < len(s1) and i2 < len(s2) and s1[i1] == s2[i2]:
                if isBuilding:
                    ret |= dp(i1+1, i2+1, False, True)
                else:
                    ret |= dp(i1+1, i2+1, False, hasBuilt)
                
            if isBuilding:
                ret |= dp(i1+1, i2, True, True)
                
            if not hasBuilt and not isBuilding:
                ret |= dp(i1+1, i2, True, True)
                
            return ret
        
        return dp(0, 0, False, False)
