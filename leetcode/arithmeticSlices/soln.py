class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        iter = 0
        ret = 0
        while iter < len(A):
            L = 2
            while iter + L < len(A):
                if A[iter+1] - A[iter] == A[iter+L] - A[iter+L-1]:
                    L += 1
                else:
                    break
                    
            if L >= 3:
                ret += (L-2)*(L-1)//2
               
            #otherwise we double count
            iter += (L-1)
            
        return ret
