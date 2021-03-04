class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #nset = set([x for x in range(len(nums)+1)])
        #return next(iter(nset - set(nums)))
        #O(1) space
        N = len(nums)
        return (N*(N+1)//2) - sum(nums)