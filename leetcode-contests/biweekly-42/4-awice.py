class Solution(object):
    def minMoves(self, A, K):
        N = len(A)
        inds = []
        for i,x  in enumerate(A):
            if x:
                inds.append(i)
        jnds = [x-i for i,x  in enumerate(inds)]
        # print("!jnds", jnds)
        P = [0]
        for x in jnds: P.append(P[-1] + x)
        
        def upper(i, j):
            # print("up", i, j)
            # print("U", P[j+1], P[i], jnds[j], i, j)
            return (j-i+1) * jnds[j] - (P[j+1] - P[i]) 
        def lower(i, j):
            # print("lo", i, j)
            return (P[j+1] - P[i]) - (j-i+1) * jnds[i]
        ans = float('inf')
        # print(inds)
        # print("P", P)
        for ix in range(len(inds) - K + 1):
            jx = ix + K - 1
            mx = ix + jx >> 1
            
            up = upper(ix, mx)
            lo = lower(mx, jx)
            # print("ulo", up ,lo , 'on', ix, jx)
            ans = min(ans, up + lo)
        return ans