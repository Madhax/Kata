class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        N = len(source)
        parent = [x for x in range(N)]
        
        def ufind(x):
            if x != parent[x]:
                parent[x] = ufind(parent[x])
            return parent[x]
        
        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)
            
            parent[ua] = ub
            
        for x, y in allowedSwaps:
            uunion(x, y)
            
        seen = [False] * N
        
        delta = collections.defaultdict(lambda: collections.Counter())
        for x in range(N):
            p = ufind(x)
            delta[p][source[x]] += 1
            delta[p][target[x]] -= 1
        
        total = 0
        for x in range(N):
            for y in delta[x].values():
                if y > 0:
                    total += y
        return total