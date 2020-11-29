"""
Hints
The queue size need not be the same as the window’s size.
Remove redundant elements and the queue should store only elements that need to be considered.
"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = deque()
        
        for x in range(0, k):
            window.append(nums[x])
            
        maxVal = max(window)
        
        output = []
        output.append(maxVal)
        
        iter = k
        while iter < len(nums):
            curNum = nums[iter]
            window.append(nums[iter])
            
            if curNum > maxVal:
                maxVal = curNum
                
            remNum = nums[iter - k]
            window.popleft()
            
            if remNum == maxVal:
                maxVal = max(window)
                
            output.append(maxVal)
            iter += 1
            
        return output