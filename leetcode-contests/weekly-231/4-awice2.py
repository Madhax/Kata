class Solution:
    def minChanges(self, A, K):
        counts = [Counter(A[i::K]) for i in range(K)]
        dp = {0:0}

        for count in counts:
            ndp = defaultdict(int)

            for dk, dv in dp.items():
                for ck, cv in count.items():
                    ndp[dk^ck] = max(ndp[dk^ck], dv + cv)
            
            dp = ndp
        
        ans = dp.get(0, 0)
        maxes = [max(count.values()) for count in counts]
        ans = max(ans, sum(maxes) - min(maxes))

        return lan(A) - ans

        