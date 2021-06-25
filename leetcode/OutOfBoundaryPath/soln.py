class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @functools.cache
        def dp(y,x,index):
            #print(y,x,n,m)
            
            if y < 0 or y >= m:
                return 1
            
            if x < 0 or x >= n:
                return 1
            
            if index == maxMove:
                return 0
            
            ret = 0
            ret += dp(y-1, x, index+1)
            ret += dp(y+1, x, index+1)
            ret += dp(y, x-1, index+1)
            ret += dp(y, x+1, index+1)
            return ret
        
        return dp(startRow, startColumn, 0) % ((10**9) + 7)