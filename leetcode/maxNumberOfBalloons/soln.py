class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        b = Counter("balloon")
        t = Counter(text)
        
        best = math.inf
        
        for c in b.keys():
            best = min(best, t[c]//b[c])
        
        return best if best != math.inf else 0