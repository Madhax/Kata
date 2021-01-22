class Solution:
    def mostCompetitive(self, A, K):
        k=len(A)-K
        stk=[]
        for x in A:
            while k and stk and stk[-1]>x:
                stk.pop()
                k-=1
            stk.append(x)
        return stk[:K]