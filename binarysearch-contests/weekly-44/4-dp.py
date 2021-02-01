class Solution:
    def solve(self, s, target):
        
        n = len(s)
        a = list(map(int, s))

        self.best = inf

        #let dp(i, t) be the recursion
        @functools.cache
        def dp(i, t):

            if i == n:
                if abs(t) < self.best:
                    self.best = abs(t)

                return self.best


            if t < -self.best:
                return math.inf

            if t < -8000:
                return math.inf

            ans = math.inf
            val = 0
            for j in range(i, min(i+4, n)):
                val = (val * 10) + a[j]

                ans = min(ans, dp(j+1, t-val))
            
            return ans

        return dp(0, target)