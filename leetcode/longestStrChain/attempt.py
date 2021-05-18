class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        d = defaultdict(list)
        maxLen = 0
        
        def CompareCounters(a, b):
            diff = 0
            for key in set(a.keys()) | set(b.keys()):
                diff += abs(a[key] - b[key])
                if diff > 1:
                    return False
            
            return True
        
        for word in words:
            d[len(word)].append(Counter(word))
        
        
        def recurse(curIndex, ctr):
            nonlocal d
            
            if curIndex == 0:
                return 0
            
            x = 0
            best = 0
            while x < len(d[curIndex]):
                if CompareCounters(d[curIndex][x], ctr):
                    best = max(best, 1 + recurse(curIndex - 1, d[curIndex][x]))
                    d[curIndex].pop(x)
                else:
                    x += 1
            
            return best
            
        best = 0
        for startingSize in sorted(d.keys(), reverse=True):
            x = 0
            while x < len(d[startingSize]):
                best = max(best, recurse(startingSize, d[startingSize][x]))
                x += 1
            
        
        return best
            
            