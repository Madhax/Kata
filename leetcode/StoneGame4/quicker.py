import math
class Solution:
    
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def canWin(n):
            bound = math.floor(math.sqrt(n))
            if bound * bound == n:
                return True
            for i in range(bound, 0, -1):
                if not canWin(n - i * i):
                    return True
            return False
        return canWin(n)
    


1-2 = -1
3-1 = 2


2-1 = 1
1-2 = 2


1
2
4



3


9+8


8