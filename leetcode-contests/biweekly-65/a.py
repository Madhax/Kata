class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        c = Counter(word1)
        d = Counter(word2)
        
        best = 0
        
        for a in c.keys():
            best = max(best, abs(c[a] - d[a]))
            
        for a in d.keys():
            best = max(best, abs(d[a] - c[a]))
            
        return best <= 3