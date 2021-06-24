import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nlargest = heapq.nlargest(4, nums)
        nsmallest = heapq.nsmallest(4, nums)
        
        return min(nlargest[3]-nsmallest[0],
                   nlargest[2]-nsmallest[1],
                   nlargest[1]-nsmallest[2],
                   nlargest[0]-nsmallest[3])