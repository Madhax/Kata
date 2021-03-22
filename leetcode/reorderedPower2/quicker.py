class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        a = 1
        N = sorted(str(N))
        while len(str(a)) < len(N): a *= 2
        while len(str(a)) == len(N):
            b = sorted(str(a))
            if b == N: return True
            a *= 2
        return False