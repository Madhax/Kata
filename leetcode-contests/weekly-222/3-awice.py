class Solution(object):
    def waysToSplit(self, A):
        N = len(A)
        MOD = 10 ** 9 + 7
        P = [0]
        for x in A: P.append(P[-1] + x)
        S = sum(A)
        
        j1 = j2 = 0
        ans = 0
        if sum(A) == 0:
            N = len(A)
            return ((N-2) * (N-1) // 2) % MOD
        P.pop(0)
        PN = len(P)
        for i in range(PN):
            if j1 <= i: j1 = i + 1
            if j2 <= i: j2 = i + 1
            if j2 <= j1: j2 = j1
                
            while j1 < PN and P[j1] - P[i] < P[i]:
                j1 += 1
            while j2 < PN and P[j2] < 2 * P[i]:
                j2 += 1
            while j2 < PN and P[j2] - P[i] <= S - P[j2]:
                j2 += 1
            # print("!", j2, j1)
            ans += j2 - j1
        return ans % MOD
