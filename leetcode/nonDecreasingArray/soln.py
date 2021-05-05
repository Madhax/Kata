class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        hasChanged = False
        currentMax = -math.inf
        for x in range(len(nums)-1):
            if nums[x+1] < nums[x]:
                if hasChanged:
                    return False
                else:
                    hasChanged = True
                    cand = min(currentMax, nums[x+1])
                    if x > 0 and cand < nums[x-1]:
                        nums[x+1] = nums[x]
                    elif cand > nums[x+1]:
                        return False
                    else:
                        nums[x] = cand
                    
                    
                    
            currentMax = max(currentMax, nums[x])
                
        return True
                    