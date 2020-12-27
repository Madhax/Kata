class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for c in S:
            if c.isalpha():
                size += 1
            else:
                size *= int(c)
       
        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1