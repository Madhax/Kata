class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @functools.cache
        def dpAlex(l, r):
            if l == r:
                return piles[l]
            
            best = -math.inf
            
            best = max(best, piles[l] + dpLee(l+1, r))
            best = max(best, piles[r] + dpLee(l, r-1))
            
            return best
        
        @functools.cache
        def dpLee(l, r):
            if l == r:
                return -piles[l]
            
            best = math.inf
            
            best = min(best, -piles[l] + dpAlex(l+1, r))
            best = min(best, -piles[r] + dpAlex(l, r-1))
            
            return best
        
        if dpAlex(0, len(piles)-1) > 0:
            return True
        
        return False