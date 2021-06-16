class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        sumSize = sum(matchsticks)
        stickSize = sumSize//4
        if sumSize % stickSize != 0:
            return False
        
        if all(val <= stickSize for val in matchsticks) == False:
            return False
            
        @functools.cache
        def GetVal(bitmask):
            val = 0
            for x in range(N):
                if bitmask >> x & 1:
                    val += matchsticks[x]
            
            return val
        
        @functools.cache
        def dp(bitmask):
            #whatever bit chosen must be at or below MOD 
            val = GetVal(bitmask)
            if val == sumSize:
                return True
            for x in range(N):
                if bitmask >> x & 1 == 0:
                    if (val//stickSize == (val + matchsticks[x])//stickSize) or (val + matchsticks[x]) % stickSize == 0:
                        if dp(bitmask | (1 << x)):
                            return True
            return False
            
        return dp(0)
            
        