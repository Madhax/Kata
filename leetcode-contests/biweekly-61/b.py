class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) & 1:
            return []
        
        
        changed.sort(reverse=True)
        
        c = Counter(changed)
        output = []
        targetSize = len(changed)//2
        
        for val in changed:
            if val in c and c[val] > 0 and val % 2 == 0 and val//2 in c and c[val//2] > 0:
                if val == 0 and c[val] == 1:
                    continue
                output.append(val//2)
                c[val] -= 1
                c[val//2] -= 1
                
        if len(output) == targetSize:
            return output
        
        return []
        
        #for val in :
            
            
        
        
