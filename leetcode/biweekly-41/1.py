class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistents = 0
        allowed = set(allowed)
        for word in words:
            isConsistent = True
            for char in word:
                if char not in allowed:
                    isConsistent = False
                    break
            
            if isConsistent:
                consistents += 1
        
        return consistents