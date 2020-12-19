from collections import deque
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        iter = 0
        low = float("inf")
        mid = float("inf")
        high = float("-inf")
        
        enditer = len(nums) - 1
        while iter <= enditer:
            if nums[iter] < low:
                if low != float("inf") and mid != float("inf"):
                    z = enditer
                    while z > iter:
                        if nums[z] > mid:
                            return True
                        z -= 1
                        
                
                low = nums[iter]
                mid = float("inf")
                high = float("-inf")
                    
            elif low < nums[iter] < mid:
                mid = nums[iter]
                    
            elif nums[iter] > mid:
                return True
                
            iter += 1
                
        return False