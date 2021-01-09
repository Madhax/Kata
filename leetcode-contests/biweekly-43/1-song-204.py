class Solution:
    def totalMoney(self, n: int) -> int:
        r = 0
        for i in range(n):
            x,y = i // 7, i % 7
            r += (x+ 1) + y
        return r