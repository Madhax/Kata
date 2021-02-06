class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2) or sorted(s1) != sorted(s2): 
            return False
        
        def helper(s1, s2):
            n = len(s1)
            if n <= 1: return s1 == s2
            if sorted(s1) != sorted(s2):
                return False
            for i in range(1, n):
                if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]):
                    return True
                if helper(s1[:i], s2[n-i:]) and helper(s1[i:], s2[:n-i]):
                    return True
            return False
        return helper(s1, s2)
            