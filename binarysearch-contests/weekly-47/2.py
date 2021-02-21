class Solution:
    def solve(self, a, b, lower, upper):
        bset = []

        for val in b:
            bset.append(val*val)

        aset = []

        for val in a:
            aset.append(val*val)

        aset.sort()
        bset.sort()
        ctr = 0
        #print(bset)
        for val in aset:
            l = bisect_left(bset, lower-val)
            r = bisect_right(bset, upper-val)
            #print(val,lower-val, upper-val, l, r)
            ctr += r-l
    
        return ctr