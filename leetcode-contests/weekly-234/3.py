import re
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        d = {}
        for (key, val) in knowledge:
            d[key] = val
            
        patterns = re.findall("\(.+?\)", s)
        
        for pattern in set(patterns):
            key = pattern[1:-1]
            if key in d:
                s = s.replace(pattern, d[key])
            else:
                s = s.replace(pattern, "?")
        #print(x)
        return s