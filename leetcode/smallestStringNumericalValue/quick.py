class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if k == 26*n:
            return "z" * n
        extra = k - n
        z_num = extra // 25
        left = extra - z_num * 25
        res = "a" * (n - z_num - 1) + chr(ord("a") + left) + "z"*z_num
        return res