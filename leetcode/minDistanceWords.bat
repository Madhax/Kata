class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        function LCSLength(X[1..m], Y[1..n])
    C = array(0..m, 0..n)
    for i := 0..m
        C[i,0] = 0
    for j := 0..n
        C[0,j] = 0
    for i := 1..m
        for j := 1..n
            if X[i] = Y[j]
                C[i,j] := C[i-1,j-1] + 1
            else
                C[i,j] := max(C[i,j-1], C[i-1,j])
    return C[m,n]
        """
        M = len(word1)
        N = len(word2)
        A = [[0 for _ in range(N+1)] for _ in range(M+1)]
        #print(A)
        for y in range(0, M):
            for x in range(0, N):
                if word1[y] == word2[x]:
                    A[y+1][x+1] = A[y][x] + 1
                else:
                    A[y+1][x+1] = max(A[y][x+1], A[y+1][x])
        #print(A)
        LCS = A[M][N]
        return (M-LCS) + (N-LCS)