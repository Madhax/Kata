class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = Counter()
        tc = Counter()
       
        for iter in range(len(s)):
            sc[s[iter]] += 1
            tc[t[iter]] += 1
           
        return sc==tc