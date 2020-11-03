class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == "(" or x == "[" or x == "{":
                stack.append(x)
                continue
            if x == ")":
                if len(stack) and stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    return False
            if x == "]":
                if len(stack) and stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False
                
            if x == "}":
                if len(stack) and stack[-1] == "{":
                    stack.pop()
                    continue
                else:
                    return False
        if len(stack):
            return False
        return True
                
                