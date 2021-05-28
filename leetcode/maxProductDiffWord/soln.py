class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        best = 0
        
        sl = []
        for word in words:
            ws = set(word)
            for (item, l) in sl:
                if any(x in item for x in ws):
                    continue
                best = max(best, len(word)*l)
            
            sl.append((ws, len(word)))
            
        return best