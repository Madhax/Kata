from itertools import *
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        for x in range(len(nums)+1):
            for val in itertools.combinations(nums, x):
                output.add(val)
        
        return output