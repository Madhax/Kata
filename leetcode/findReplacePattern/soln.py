class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def buildMap(val):
            key = 0
            seen = set()
            d = defaultdict(int)
            mapping = ""
            for c in val:
                if c in seen:
                    #print(d)
                    mapping += str(d[c])
                else:
                    seen.add(c)
                    d[c] = key
                    mapping += str(key)
                    key += 1
                    
            
            return mapping
    
        d = defaultdict(list)
        for word in words:
            d[buildMap(word)].append(word)
            
        return d[buildMap(pattern)]
        #for word in words:
            #print(buildMap(word))
            
        return []