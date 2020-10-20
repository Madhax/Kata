class Solution(object):
    def trimMean(self, A):
        A.sort()
        N = len(A)
        K = N // 20
        A = A[K:-K]
        S = sum(A)
        N = len(A)
        return S /float(N)