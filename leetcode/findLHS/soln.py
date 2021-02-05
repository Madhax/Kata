from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter()
       
        for x in nums:
            c[x] += 1
           
        longest = 0
       
        for key in c.keys():
            if c[key] > 0 and c[key-1] > 0:
                longest = max(longest, c[key] + c[key-1])
           
        return longest
