from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        i,j = 0,0
        
        maxVal = 0
        while j < len(s):
            if d[s[j]] == 0:
                d[s[j]] += 1
                j += 1
                if j - i > maxVal:
                    print(s[i:j], d)
                    maxVal = j-i
            else:
                while d[s[j]] > 0:
                    d[s[i]] -= 1
                    i += 1
                    
        return maxVal
                
        
        