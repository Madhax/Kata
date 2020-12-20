class Solution(object):
    def maximumUniqueSubarray(self, A):
        N = len(A)
        P = [0]
        for x in A: P.append(P[-1] + x)
        import collections
        count = collections.Counter()
        ans = i = 0
        for j, x in enumerate(A):
            count[x] += 1
            while count[x] >= 2:
                count[A[i]] -= 1
                i += 1
            ans = max(ans, P[j + 1] - P[i])
        return ans