class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        
        if N == 1:
            return 0
        
        up = 2
        while up <= N:
            up = up << 1
            
        return up-1-N