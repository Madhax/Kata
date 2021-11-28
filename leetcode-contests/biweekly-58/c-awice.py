class Solution:
    def minSpaceWastedKResizing(self, A, K):
        N = len(A)
        @cache
        def dp(i, rem):
            if i >= N: return 0
            if rem == 0:
                s = 0
                m = -inf
                t = 0
                for j in range(i, N):
                    s += A[j]
                    m = max(m, A[j])
                    t += 1
                return m * t - s
            
            s = t = 0
            m = -inf
            ans = inf
            for j in range(i, N):
                s += A[j]
                t += 1
                m = max(m, A[j])
                # print("i rem", i, rem, "j", j, "m t s", m, t, s, 'of ', dp(j + 1, rem - 1))
                ans = min(ans, m * t - s + dp(j + 1, rem - 1))
            return ans
        
        # print(dp(2, 0))
        return dp(0, K)
