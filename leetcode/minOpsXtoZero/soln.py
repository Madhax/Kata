from collections import deque
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if total < x:
            return -1
        if total == x:
            return len(nums)
   
        target = total - x
       
        i, j = 0, 0
        curTotal = 0
        bestRange = -1
        #print(target)
        while j < len(nums):
            curTotal += nums[j]
           
            while curTotal > target:
                curTotal -= nums[i]
                i += 1
               
            if curTotal == target and j-i > bestRange:
                bestRange = j-i+1
               
            j += 1
           
        if bestRange < 0:
            return -1
        return len(nums)-bestRange
