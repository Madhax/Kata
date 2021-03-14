class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
       
        arr.sort()
        arrset = set(arr)
        d = defaultdict(int)
        for val in arr:
            d[val] = 1
            for x in arr:
                if x >= val:
                    break
                   
                mult = val / x
                if mult != val // x:
                    continue
                   
                if mult in arrset:
                    d[val] += d[mult] * d[x]
       
        ctr = 0
        for x in arr:
            ctr += d[x]
        print(ctr)
        return ctr % (10**9 + 7)
