from collections import deque
class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        end = nums.copy()
        end.sort()
        
        d = deque(nums)
        minVal = min(nums)
        minPosn = nums.index(minVal)
        
        d.rotate(-minPosn)
        N -= minPosn
        
        for x in range(N):
            if list(d) == end:
                return True
            
            d.append(d.popleft())
        return False
        #return list(d)
        