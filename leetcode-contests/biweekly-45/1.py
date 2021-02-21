from collections import *
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = Counter()
        for x in nums:
            d[x] += 1
            
        #print(d)
        return sum([x for x in d.keys() if d[x] == 1])