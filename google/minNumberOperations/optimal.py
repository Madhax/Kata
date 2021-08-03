class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        prev = 0
        
        calc = 0
        for x in target:
            if x - prev > 0:
                calc += (x-prev)
                
            prev = x
            
        return calc