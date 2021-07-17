class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        d = defaultdict(set)
        
        for idx, val in enumerate(nums):
            d[val].add(idx)
            
        output = []
        seen = set()
        
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    complement = target - (nums[x]+nums[y]+nums[z])
                    cand = (nums[x],nums[y],nums[z],complement)
                    if complement < nums[z]:
                        continue
                        
                    elif cand not in seen and complement in d and any(idx > z for idx in d[complement]):
                        output.append(list(cand))
                        seen.add(cand)
                        
        return output