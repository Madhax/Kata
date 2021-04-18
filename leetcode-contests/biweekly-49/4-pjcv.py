class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        mods = [0 for _ in range(10)]
        for g in groups:
            mods[g % batchSize] += 1
            
        @functools.lru_cache(maxsize=None)
        def h(mods, currmod):
            if sum(mods) == 0:
                return 0
            
            result = 0
            if currmod == 0:
                result += 1
                
            best = 0
            for i in range(10):
                if mods[i]:
                    new_mods = tuple(mods[j] if j != i else mods[j] - 1 for j in range(10))
                    best = max(best, h(new_mods, (currmod + i) % batchSize))
            return best + result
            
        return h(tuple(mods), 0)