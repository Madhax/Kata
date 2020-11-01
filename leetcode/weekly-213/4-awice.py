class Solution(object):
    def kthSmallestPath(self, A, K):
        R, C = A
        @lru_cache(None)
        def binom(n, k):
            r = 1
            for i in range(1,k+1):
                r *= n- i + 1
                r //= i
            return r
        
        ans = []
        K -= 1
        N = R+C
        horis = C
        verts = R
        while len(ans) < N:
            rseqs = binom(horis+verts-1, verts)
            # print("!", rseqs, horis,verts)#, cs)
            if K < rseqs and horis:
                ans.append('H')
                horis -= 1
            else:
                K -= rseqs
                ans.append('V')
                verts -= 1
        return "".join(ans)
        
