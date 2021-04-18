class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = 1
        for x in range(1, maximumBit):
            mask = (mask << 1) | 1
        
        #print(mask)
        #return []
        precalc = [nums[0]]
        for x in range(1, len(nums)):
            precalc.append(nums[x]^precalc[-1])
        
        output = []
        while len(precalc) > 0:
            #if len(precalc) == 1:
            #    output.append(~precalc[0] & mask)
            #    continue
                
            val = precalc.pop()
            output.append(~val & mask)
            
        return output
        #max xor is one that optimizes all digits
