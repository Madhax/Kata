class Solution(object):
    def canFormArray(self, A, pieces):
        first = {}
        for row in pieces:
            first[row[0]] = row
        
        i = 0
        while i < len(A):
            x = A[i]
            if x not in first: return False
            row = first[x]
            for j,y in enumerate(row):
                if i == len(A): return False
                if A[i] != y: return False
                i += 1
        
        return True