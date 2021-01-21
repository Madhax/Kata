class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for p in s:
            if p == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop()
            
            elif p == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop()
            
            elif p == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                stack.pop()
            else:
                stack.append(p)
                
        return len(stack) == 0
            