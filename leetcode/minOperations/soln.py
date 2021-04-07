class Solution:
    def minOperations(self, n: int) -> int:
        x = n // 2
        return x * (n-x)