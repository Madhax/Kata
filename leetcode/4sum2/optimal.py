class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if len(A) == 0:
            return 0
        
        m1 = {}
        for a in A:
            if a in m1:
                m1[a] += 1
            else:
                m1[a] = 1
        m2 = {}
        for a, v in m1.items():
            for b in B:
                ab = a + b
                if ab in m2:
                    m2[ab] += v
                else:
                    m2[ab] = v
        
        m3 = {}
        for c in C:
            if c in m3:
                m3[c] += 1
            else:
                m3[c] = 1
        
        res = 0
        for c, v in m3.items():
            for d in D:
                cd = - c - d
                if cd in m2:
                    res += m2[cd] * v
                
        return res