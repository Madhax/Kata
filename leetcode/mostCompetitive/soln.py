from collections import deque
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
       
        #monostack
        N = len(nums)
        if N < k: return []
        s = deque()
        iter = 0
        S = 0
        while iter < len(nums):
            #print(nums[iter], iter, len(s), len(nums))
            while S and s[-1] > nums[iter] and (k-S) < (N - iter):
                s.pop()
                S -= 1
               
            if len(s) < k:
                s.append(nums[iter])
                S += 1
               
            iter += 1
           
        return s