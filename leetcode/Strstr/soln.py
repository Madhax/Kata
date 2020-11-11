class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        if haystack == needle:
            return 0
       
        if set(needle).issubset(set(haystack)) == False:
            return -1
       
        while i < len(haystack):
            j = 0
            while j+i < len(haystack) and j < len(needle):
                if haystack[i+j] != needle[j]:
                    break
                j += 1
           
            if j == len(needle):
                return i
       
            i += 1
           
        return -1