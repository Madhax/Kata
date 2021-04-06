class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for x in range(len(A)):
            if abs(x-A[x]) > 1:
                return False
        return True
    