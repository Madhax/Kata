class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        def primes(n):
            primfac = []
            d = 2
            while d*d <= n:
                while (n % d) == 0:
                    primfac.append(d)  # supposing you want multiple factors repeated
                    n //= d
                d += 1
            if n > 1:
                primfac.append(n)
            return primfac
        res=[]
        from math import comb
        for q in queries:
            ct=1
            L=primes(q[1])
            D={}
            for x in L:
                if x in D:
                    D[x]+=1
                else:
                    D[x]=1
            for x in D:
                ct=(ct*comb(D[x]+q[0]-1, q[0]-1))%(10**9+7)
            res.append(ct)
        return res
                
