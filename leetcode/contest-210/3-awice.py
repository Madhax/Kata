class Solution(object):
    def checkPalindromeFormation(self, S, T):
        # if S[..i] + T[j..]  is a palindrome  or 
        def pali(A, i, j):
            if i >= j: return True
            for k in xrange(j -i+ 1):
                if A[i+k] != A[j-k]: return False
            return True
        N = len(S)
        i = 0
        j = N - 1
        while i < j and S[i] == T[j]:
            i += 1
            j -= 1
        if pali(S, i, j) or pali(T, i, j):
            return True
        
        i = 0
        j = N - 1
        while i < j and T[i] == S[j]:
            i += 1
            j -= 1
        
        if pali(S, i, j) or pali(T, i, j):
            return True
        return False
