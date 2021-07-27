import bisect
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        best = math.inf
        bestDelta = math.inf
        #print(nums)
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                cand = -((nums[x] + nums[y]) - target)
                idx = bisect.bisect_left(nums, cand)
                
                if idx > 0:
                    if abs(nums[idx-1] - cand) < bestDelta and idx != x+1 and idx != y+1:
                        bestDelta = abs(nums[idx-1]-cand)
                        best = nums[x] + nums[y] + nums[idx-1]
                        #print(x,y,idx)
                
                if idx < len(nums):
                    if abs(nums[idx] - cand) < bestDelta and idx != x and idx != y:
                        bestDelta = abs(nums[idx]-cand)
                        best = nums[x] + nums[y] + nums[idx]
                        #print(x,y,idx)
        
        return best
                
                        
                    
                