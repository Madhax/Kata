class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c = collections.Counter(nums)
        cv = list(c.values())
        M = len(cv)
        N = len(quantity)
        
        cache = [0] * (1 << N)
        for i in range(1 << N):
            for j in range(N):
                if ((1 << j) & (i)) > 0:
                    cache[i] += quantity[j]
        
        @lru_cache(None)
        def go(index, mask):
            if mask == 0:
                return True
            if index == M:
                return False
            
            i = mask
            while i > 0:
                total = cache[i]
                if total <= cv[index] and go(index + 1, mask ^ i):
                    return True
                
                i = (i - 1) & mask
            
            return go(index + 1, mask)
        
        return go(0, (1 << N) - 1)