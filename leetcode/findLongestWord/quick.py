class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        result = ""
        for w in d:
            diff = len(w) - len(result)
            if diff >= 0:
                if diff > 0 or w < result:
                    try:
                        pos = -1
                        for c in w:
                            pos = s.index(c, pos + 1)
                        result = w
                    except ValueError:
                        pass        
        return result