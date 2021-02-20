class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        output = []
        openBraces = []
        
        for x in s:
            if x == "(":
                output.append(x)
                openBraces.append((len(output)))
            elif x == ")" and len(openBraces) > 0:
                output.append(x)
                openBraces.pop()
            elif x != ")":
                output.append(x)
                
        #print(openBraces)
        for offset, index in enumerate(openBraces):
            output.pop(index-offset-1)
            
        return "".join(output)