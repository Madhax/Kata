class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        maxDepth = 0
        for x in range(0, len(s)):
            if s[x] == "(":
                counter += 1
                if maxDepth < counter:
                    maxDepth = counter
            elif s[x] == ")":
                counter -= 1
                
        return maxDepth