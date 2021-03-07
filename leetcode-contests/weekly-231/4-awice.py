class Solution(object):
    def minChanges(self, A, K):
        from collections import Counter, defaultdict as ddic
        groups = []
        lengths = []
        for i in range(K):
            B = A[i::K]
            sl = Counter(B)
            groups.append(sl)
            lengths.append(len(B))
        
        dp = {0: 0}
        for i, grp in enumerate(groups):
            ndp = ddic(int)
            for gk, gv in grp.iteritems():
                for k, v in dp.iteritems():
                    ndp[k ^ gk] = min(ndp[k ^ gk], v - gv)
            dp = ndp
        
        base = float('inf')
        if 0 in dp:
            base = dp[0] + len(A)
        bigs = [max(grp.values()) for grp in groups]
        cand = float('inf')
        base2 = len(A) - sum(bigs)
        # print("B", bigs, base, base2)
        for i, b in enumerate(bigs):
            l = lengths[i]
            cand2 = base2 + b
            # print("!", i,l,b)
            if cand2 < cand: cand=cand2
        return min(base, cand)
                
        """
        base = 0
        vals = []
        valxor = 0
        for i, grp in enumerate(groups):
            l = lengths[i]
            mi = max(grp, key=grp.__getitem__)
            m = grp[mi]
            base += l - m
            vals.append(mi)
            valxor ^= mi
        
        if valxor == 0:
            return base
        
        ans = float('inf')
        for i, grp in enumerate(groups):
            l = lengths[i]
            mi = vals[i]
            m = grp[mi]
            valcand = valxor ^ mi
            oldcost = l - m
            cost = l - grp[valcand]
            cand = base - oldcost + cost
            if cand<ans:ans=cand
        return ans
        """
        
        
            