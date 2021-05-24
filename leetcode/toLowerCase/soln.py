class Solution:
    def toLowerCase(self, s: str) -> str:
        #return s.lower()
        s = list(s)
        for index, c in enumerate(s):
            if'A' <= c <= 'Z':
                s[index] = chr(ord('a') + (ord(c) - ord('A')))
        
        return "".join(s)