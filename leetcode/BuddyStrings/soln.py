class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        maxDiff = 0
        ad = {}
        duplicates = False
        indices = []
        for x in range(len(A)):
            if A[x] != B[x]:
                maxDiff += 1
                indices.append(x)
            if A[x] not in ad:
                ad[A[x]] = 1
            else:
                duplicates = True
        if maxDiff == 2:
            if A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]:
                return True
            return False
        
        if A == B and duplicates:
            return True
        
        return False