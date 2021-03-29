class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        diff = 0
        iter = 0
        diffIndices = []
        s1 = list(s1)
        s2 = list(s2)
        while iter < len(s2):
            if s1[iter] != s2[iter]:
                diff += 1
                diffIndices.append(iter)
            iter += 1
                
        if len(diffIndices)  == 0:
            return True
        
        if len(diffIndices) > 2:
            return False
        
        if len(diffIndices) == 2:
            s2[diffIndices[0]], s2[diffIndices[1]] = s2[diffIndices[1]], s2[diffIndices[0]]
            return s1 == s2
        
        return False