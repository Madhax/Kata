from collections import deque

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        iter = 0
        best = 0
        
        slidingWindow = deque()
        s = set()
            
        for x in nums:
            if x in s:
                val = sum(s)
                    
                if val > best:
                    best = val
                        
                while len(slidingWindow) > 0:
                    popval = slidingWindow.popleft()
                    if popval == x:
                        slidingWindow.append(x)
                        break
                    
                    s.remove(popval)
            else:
                s.add(x)
                slidingWindow.append(x)
        
        val = sum(s)
        if val > best:
            return val
        else:
            return best
                        
            
                