class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        
        curk = 1
        for cand in arr:
            if c[cand] == 1 and curk == k:
                return cand
            elif c[cand] == 1:
                curk += 1
                
            
        return ""
