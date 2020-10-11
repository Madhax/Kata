class Solution(object):
    def maximalNetworkRank(self, N, edges):
        A = [set() for _ in xrange(N)]
        for i, (u, v) in enumerate(edges):
            A[u].add(i)
            A[v].add(i)
        
        ans = 0
        for u in xrange(N):
            for v in xrange(u + 1, N):
                bns = len(A[u]) + len(A[v])
                for ei in A[u]:
                    if ei in A[v]:
                        bns -= 1
                if bns > ans:
                    ans = bns
        return ans