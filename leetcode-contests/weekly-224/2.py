from collections import defaultdict
from math import comb
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        s = set(nums)
        d = defaultdict(int)
        
        i,j = 0,0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                d[nums[i]*nums[j]] += 1 
                #print(nums[i], nums[j], nums[i]*nums[j])
                j += 1
            i += 1
            
        
        output = sum([comb(x,2)*8 for x in d.values() if x >= 2])
        
        #print(d)
        return output
        
        """
        i,j,k = 0,0,0
        ctr = 0
        
        
        
        while i < len(nums)+1//2:
            j = i + 1
            while j < len(nums):
                k = j + 1
                while k < len(nums):
                    val = nums[i]*nums[j]/nums[k]
                    if val in s:
                        print(nums[i], nums[j], nums[k], val)
                        ctr += 8
                    k += 1
                j += 1
            i += 1
        
        return ctr"""