class Solution:
    def minimumMountainRemovals(self, A: List[int]) -> int:
        @lru_cache(None)
        def dp(i):
            ans = 1
            for h in range(i):
                if A[h] < A[i]:
                    bns = dp(h) + 1
                    if bns > ans: ans = bns
            return ans
        
        @lru_cache(None)
        def ep(i):
            if i == N-1: return 1
            ans = 1
            for j in range(i+1, len(A)):
                if A[j] < A[i]:
                    bns = ep(j) + 1
                    if bns > ans: ans = bns
            return ans
        
        N=len(A)
        # for i in range(N):
        #     print("!", dp(i), ep(i), N+1-dp(i)-ep(i))
        return N +1 - max(dp(i) + ep(i) for i in range(1, N-1))