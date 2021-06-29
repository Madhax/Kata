class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        iter = 1
        while iter < len(s):
            if s[iter] == s[iter-1]:
                s.pop(iter-1)
                s.pop(iter-1)
                
                iter = max(1, iter - 1)
                
            else:
                iter += 1
        return "".join(s)