class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3: return False
        inc = A[0] < A[1]
        k = 0
        for i in range(1, n):
            if inc and A[i-1] >= A[i]: 
                k += 1
                inc = False
            if not inc and A[i-1] <= A[i]:
                return False
        return k == 1