class Solution:
    def makeFancyString(self, s: str) -> str:
        
        output = []
        
        prevSame = 0
        prevChar = None
        
        for c in s:
            if c == prevChar:
                if prevSame == 2:
                    continue
                
                output.append(c)
                prevSame += 1
            else:
                prevSame = 1
                prevChar = c
                output.append(c)
                
        return "".join(output)
