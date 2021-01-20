class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        def maxPalindrome(index):
            nonlocal s
           
            start, end = index, index +1
            print(index)
            #evens
            while start >= 0 and end < len(s) and  s[start] == s[end]:
                start -= 1
                end += 1
               
            if start < 0 or end == len(s):
                start += 1
                end -= 1
               
            elif s[start] != s[end]:
                start += 1
                end -= 1
               
            scand, ecand = start, end
           
            #print("!" , "evens", scand, ecand)
           
            start, end = max(index-1, 0), min(index + 1, len(s)-1)
            while start >= 0 and end < len(s) and  s[start] == s[end]:
                start -= 1
                end += 1
               
            if start < 0 or end == len(s):
                start += 1
                end -= 1
               
            elif s[start] != s[end]:
                start += 1
                end -= 1
                   
            #print("!", "odds", start, end)
               
            if ecand-scand > end-start:
                return (scand, ecand)
            else:
                return (start,end)
               
        best = 0
        start, end = 0, 0
        for index in range(len(s)):
            (startcand,endcand) = maxPalindrome(index)
           
            if endcand-startcand > best:
                start=startcand
                end = endcand
                best = end-start
               
        #print(start, end)
        return s[start:end+1]
