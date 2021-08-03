class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @functools.cache
        def dpAlice(index):
            if index  == len(stoneValue):
                return 0
            
            best = -math.inf
            cand = 0
            for x in range(3):
                if index + x == len(stoneValue):
                    break
                cand += stoneValue[index + x]
                best = max(best, cand + dpBob(index + x + 1))
                
            return best
            
        @functools.cache
        def dpBob(index):
            if index  == len(stoneValue):
                return 0
            
            best = math.inf
            cand = 0
            for x in range(3):
                if index + x == len(stoneValue):
                    break
                cand -= stoneValue[index + x]
                best = min(best, cand + dpAlice(index + x + 1))
                
            return best
        
        ret = dpAlice(0)
        if ret > 0:
            return "Alice"
        if ret < 0: 
            return "Bob"
        
        return "Tie"