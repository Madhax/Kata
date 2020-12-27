class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        concatSize = sum([len(x) for x in words])
        words = set(words)
        #print(concatSize)
        output = []
        if concatSize > len(s):
            return output
        
        iter = 0
        maxSize = concatSize
        while maxSize <= len(s):
            slidingWindow = s[iter:maxSize]
            #print(slidingWindow)
            
            validIndex = True
            for word in words:
                if word not in slidingWindow:
                    validIndex = False
                    break
                    
            if validIndex:
                output.append(iter)
            
            iter += 1
            maxSize += 1
        
        return output
        