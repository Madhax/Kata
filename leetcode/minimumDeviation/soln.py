class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        #between lowest odd number and highest odd number
        
        newnums = nums.copy()
        
        for index in range(len(newnums)):
            while newnums[index] % 2 == 0:
                newnums[index] /= 2
                
        maxNum = max(newnums)
        minNum = min(newnums)
        #print(newnums)
        for index in range(len(newnums)):
            while newnums[index]*2 < maxNum and (newnums[index] < nums[index] or newnums[index] % 2 == 1):
                newnums[index] *= 2
                
        possibleBest = int(max(newnums) - min(newnums))
        #print(newnums)
        
        minNum = min(newnums)
        while minNum < maxNum:
            changed = False
            for index in range(len(newnums)):
                if newnums[index] == minNum and (newnums[index] < nums[index] or newnums[index] % 2 == 1):
                    newnums[index] *= 2
                    changed = True
                    
            if changed:
                minNum = min(newnums)
            
                possibleBest = min(possibleBest, int(max(newnums) - min(newnums)))
            else:
                break
        
        return possibleBest
        #print(newnums)
        
        #print(lowodd, highodd)    
        #return 
        
        
        
        #return 0
    