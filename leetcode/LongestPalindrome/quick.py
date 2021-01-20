class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxl = 1
        l = len(s)
        if s == s[::-1]:
            return s
        else:
            for i in range(1, l):
                odd = s[i-maxl-1:i+1]
                even = s[i-maxl:i+1]
                if (i - maxl - 1) >= 0 and odd == odd[::-1]:
                    start = i - maxl - 1
                    maxl = maxl + 2
                    continue
                if even == even[::-1]:
                    start = i - maxl
                    maxl = maxl + 1
            return s[start:start+maxl]
