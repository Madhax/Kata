def mult(A: list[list[int]], B: list[list[int]]):
    C = []
    for i in range(5):
        C.append([0,0,0,0,0])
    
    for i in range(5):
        for j in range(5):
            for k in range(5):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] = C[i][j] % (10**9+7)
                
                
    return C

def power(A,n):
    if n == 0:
        return [[1, 0, 0, 0, 0,],[0, 1, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 0, 1, 0],[0, 0, 0, 0, 1]]
    sqrt = power(A,n//2)
    sqrt = mult(sqrt,sqrt)
    if n%2 == 0:
        return sqrt
    else:
        return mult(sqrt,A)
    
def entrySum(A):
    tot = 0
    for i in range(5):
        for j in range(5):
            tot += A[i][j]
    return tot % (10**9+7)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        A = [[0, 1, 0, 0, 0,],[1, 0, 1, 0, 0],[1, 1, 0, 1, 1],[0, 0, 1, 0, 1],[1, 0, 0, 0, 0]]
        
        return entrySum(power(A,n-1)) 