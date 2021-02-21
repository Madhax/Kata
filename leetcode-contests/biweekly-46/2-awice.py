class Solution:
    def canChoose(self, groups, A):
        @functools.cache
        def dp(i, j):
            if i == len(groups):
                return True
            if j >= len(A):
                return False
            if dp(i, j+1):
                return True
            if all(j+k < len(A) and A[j+k] == x for k,x in enumerate(groups[i])):
                return dp(i+1, j+len(groups[i]))
            return False
        
        return dp(0,0)