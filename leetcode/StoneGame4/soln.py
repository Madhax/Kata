import functools
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def isSquare(number):
             return number == math.isqrt(number) ** 2
        
        @lru_cache(maxsize=None)
        def hasPathToWinning(stones):
            if stones == 0:
                return 0
            
            if isSquare(stones):
                return True
        
            canWin = False
            sqr = 1
            take = 1
            while take < stones:
                if hasPathToWinning(stones-take) == False:
                    return True
                
                sqr += 1
                take = sqr**2
                
            return canWin
                
        
        
        return hasPathToWinning(n)
        