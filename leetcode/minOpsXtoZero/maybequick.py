class Solution:
    def minOperations(self, A, x):
        N=len(A)

        tt=sum(A)
        if tt<x:
            return -1
        if tt==x:
            return N

        target=tt-x
        cur=0
        ans=-1
        i=k=0
        for x in A:
            cur+=x
            k+=1
            while cur>target:
                cur-=A[i]
                i+=1
                k-=1
            if cur==target and k>ans:
                ans=k

        return -1 if ans==-1 else N-ans