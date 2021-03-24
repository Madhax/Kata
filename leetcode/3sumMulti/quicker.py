class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = collections.Counter(arr)
        
        res = 0 
        if target % 3 == 0: 
            n = c.get(target // 3, 0) 
            res += n * (n-1) * (n-2) // 6
            
        keys = sorted(c.keys())
        for k in keys: 
            n = c[k]
            if n > 1 and k < target and target - 2 * k != k: 
                res += c.get(target - 2 * k, 0) * n * (n-1) // 2  
        
        for i in range(len(keys)):
            if keys[i] >= target // 3: break
            for j in range(i+1, len(keys)): 
                new = target - (keys[i] + keys[j])
                if new <= keys[j]: break
                if new in c: 
                    res += c[keys[i]] * c[keys[j]] * c[new]
            
        return res % (10**9 + 7)