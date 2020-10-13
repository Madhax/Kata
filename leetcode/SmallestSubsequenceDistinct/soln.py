class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        lastIndex = {}
        for i, c in enumerate(s):
            #print(i,c)
            lastIndex[c] = i
            
        output = []
        chars = set()
        
        for x in range(0, len(s)):
            if s[x] not in chars:
                while len(output) and s[x] < output[-1] and lastIndex[output[-1]] > x:
                    chars.remove(output[-1])
                    output.pop()
                
                
                output.append(s[x])
                chars.add(s[x])
                
        return "".join(output)