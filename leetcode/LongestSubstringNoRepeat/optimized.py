class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxlen=0
        start=0
        seen={}

        
        for i,char in enumerate(s):
            
            if char in seen and start<=seen[char]:
                start=seen[char]+1
                
            else:
                maxlen=max(maxlen,i-start+1)
            
            seen[char]=i
        
        return maxlen
            
            