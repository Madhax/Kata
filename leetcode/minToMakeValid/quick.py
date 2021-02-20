class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Time complexity: O(n)
        # Space complexity: O(n) put all chars on stack
        
        s = list(s)
        
        stack = []       
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)