class Solution:
    def numSplits(self, s: str) -> int:
        ctr2 = Counter(s)
        set1 = set()
        set2 = set(s)
        
        goodsplits = 0
        for val in s:
            ctr2[val] -= 1
            if ctr2[val] == 0:
                set2.remove(val)
                
            set1.add(val)
            
            if len(set1) == len(set2):
                goodsplits += 1
                
        return goodsplits