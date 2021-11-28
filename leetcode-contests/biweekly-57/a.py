class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        d = Counter(s)
        
        val = list(d.values())[0]
        
        return all(num == val for num in d.values())