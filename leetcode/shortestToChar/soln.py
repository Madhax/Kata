class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        """
        indices = []
        for index, ch in enumerate(s):
            if ch == c:
                indices.append(index)
                
        print(indices)
        output = []
        for index in range(len(s)):
            output.append(abs(index - indices[min(range(len(indices)), key = lambda i: abs(indices[i]-index))]))
            
        """
        
        output = [math.inf ] *len(s)
        #print(output)
        lastIndex = -math.inf
        for x in range(len(s)):
            if s[x] == c:
                lastIndex = x
            
            output[x] = min(output[x], x-lastIndex)
            
        lastIndex = math.inf
        for x in range(len(s)-1, -1, -1):
            if s[x] == c:
                lastIndex = x
                
            output[x] = min(output[x], lastIndex-x)
            
        return output
