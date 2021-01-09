class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        l = 2 * n - 1
        a = [0] * l
        cand = set(range(1,n+1))
        def dfs(i, cand):
            while i<l and a[i]:
                i += 1
            if i >= l:
                return True
            for x in sorted(cand, reverse=True):
                if x == 1:
                    a[i] = x
                    if dfs(i+1, cand - {x}):
                        return True
                    a[i] = 0
                elif i+x < l and a[i+x] == 0:
                    a[i] = a[i+x] = x
                    if dfs(i+1, cand - {x}):
                        return True
                    a[i] = a[i+x] = 0
        dfs(0, cand)
        return a